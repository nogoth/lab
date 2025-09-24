import asyncio
from typing import TypedDict, Annotated, List, Union
import operator

from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage, BaseMessage, ToolMessage
from langchain_core.tools import BaseTool
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, create_react_agent

from fastmcp import Client
from langchain_mcp_adapters.tools import load_mcp_tools

# --- 1. Define the Agent's State (The 'memory' of the graph) ---
# This is crucial in LangGraph. All data flows through this state.
class AgentState(TypedDict):
    # 'messages' is the core of the state, holding the conversation history
    # 'operator.add' tells LangGraph to APPEND new messages instead of overwriting
    messages: Annotated[List[BaseMessage], operator.add]
    
    # You can add other keys like 'current_tool_name' if needed

def call_model(state: AgentState, agent_chain: callable) -> dict:
    # Get the conversation history from the state
    messages = state["messages"]
    response = agent_chain.invoke({"messages": state["messages"]})
    # The output is a dict that updates the state
    return {"messages": [response]}

# --- 3. The Routing Logic (The 'Decision Maker') ---
def should_continue(state: AgentState) -> str:
    """Decides whether to continue the loop."""
    last_message = state["messages"][-1]

    print(f"Type: {last_message.type}")
    print(f"Tool calls: {last_message.tool_calls}")
    print(f"Content: {last_message.content} {len(last_message.content)}")

    # 1. Check if the LLM is requesting tool use.
    if isinstance(last_message, AIMessage) and last_message.tool_calls:
        return "tools"
    
    # 2. Check if the LLM provided a final answer (i.e., content exists).
    # This assumes the LLM has generated a response that is NOT a tool call.
    if last_message.content: # and len(last_message.content) < 15:
        return "end" #doesn't work if it has a thinking box
        
    # 3. Fallback/Error: If it's a ToolMessage or an empty AIMessage, loop back to the agent.
    # This shouldn't be necessary if the previous steps work, but acts as a safeguard.
    #  return "agent" 
    return "agent"

SYSTEM_PROMPT=(
    "You are an excellent assistant. You have access to the following tools. "
    "To fulfill a user request, you should first analyze the user's intent. "
    "If a tool is required, generate the appropriate tool call. "
    "If the request is complete or can be answered directly, provide a final, "
    "natural language response."
)
SYSTEM_PROMPT2=(
   "You are an excellent assistant with access to tools. Your primary goal is to "
    "fulfill the user's request. **Analyze the history carefully.**"
    
    "\n\n--- ACTION RULES ---"
    "1. **TO MAKE A TOOL CALL**: You MUST ONLY output the structured tool call in the `tool_calls` list. The main `content` field MUST be empty or contain only a brief, necessary internal thought."
    
    "2. **TO PROVIDE A FINAL ANSWER**: After a tool has executed and returned its OBSERVED result (a ToolMessage), or if no tool is needed, you MUST provide a concise, final, natural language answer. This final response MUST have a non-empty `content` field and a **completely EMPTY `tool_calls` list ([]).** DO NOT GENERATE ANY TOOL CALLS IN YOUR FINAL RESPONSE."
    
    "\n\n--- TERMINATION INSTRUCTION ---"
    "If the last message in the history is a ToolMessage (Observation), your next response MUST be the final answer."
)

async def next_lines(n: int, prev: str, app) -> str:
    prompt = f"Generate the next {n} lines of a story using ```{prev}```"
    state = await app.ainvoke({"messages": [HumanMessage(content=prompt)]})
    return state["messages"][-1].content

async def talkToServer():
    print("Initializing LangGraph Agent...")
    model_name = "qwen3:1.7b" # Use a model with good tool-calling ability
    
    client = Client("http://localhost:8000/mcp")
    async with client:
        # Load tools from the MCP server
        tools: List[BaseTool] = await load_mcp_tools(client.session)
        print(f"Loaded tools: {[tool.name for tool in tools]}")
        
        # Instantiate the LLM
        llm = ChatOllama(model=model_name, temperature=0.1,reasoning=False)#? maybe?
        
        # Bind the tools to the LLM (crucial step for the LLM to know its tools)

        prompt_template = ChatPromptTemplate.from_messages( [ SystemMessage(content=SYSTEM_PROMPT), # <-- Insert the new prompt here
                                                             ("placeholder", "{messages}"), # The message history placeholder for LangGraph
                                                             ])

        #create an agent_runnable 
        agent_runnable = prompt_template | llm.bind_tools(tools)

        # --- 4. Define the Nodes and Edges (The State Machine) ---
        workflow = StateGraph(AgentState)

        # Node A: The LLM/Agent's thinking and action selection
        workflow.add_node("agent", lambda state: call_model(state,agent_runnable))
        
        # Node B: The Tool Executor (LangGraph's pre-built handler)
        # This node handles parsing the tool call and running the function.
        workflow.add_node("tools", ToolNode(tools))

        workflow.set_entry_point("agent")

        # Add the conditional edge for routing after the agent runs, call 'should_continue' to decide where to go
        workflow.add_conditional_edges(
            "agent",
            should_continue,
            {
                "tools": "tools", # If tool_calls exist, go to 'tools' node
                "end": END        # If no tool_calls, go to the 'END'
            },
        )

        # After the tools run, they must go back to the agent to summarize the results
        workflow.add_edge("tools", "agent")

        app = workflow.compile()

        await app.ainvoke({"messages": [HumanMessage(content="Speak the answer to the question `What is the capital of Belgium`")]})
        await app.ainvoke({"messages": [HumanMessage(content="Speak the answer to the question `What is the capital of Canada and talk about three restaurants there?`")]})
        
        user_input = "Please use the speak_it tool to say 'Welcome to LangGraph, it works!'"
        final_state = await app.ainvoke({"messages": [HumanMessage(content=user_input)]})

        final_state = await app.ainvoke({"messages": [HumanMessage(content="Generate the first two lines of a story. Generate three key elements on your own.")]})
        
        print(final_state)
        final_response = final_state["messages"][-1].content
        final_state = await app.ainvoke({"messages": [HumanMessage(content=f"Generate the next two lines of a story using ```{final_response}```")]})

        f = await next_lines(2,final_state["messages"][-1].content, app)
        f = await next_lines(2,f, app)
        f = await next_lines(2,f, app)
        print("\n--- Final Agent Response ---")
        print(final_response)
        
if __name__ == "__main__":
    asyncio.run(talkToServer())
