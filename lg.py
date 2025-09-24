import asyncio
from typing import TypedDict, Annotated, List, Union
import operator

# LangChain/Ollama imports
from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage, BaseMessage, ToolMessage
from langchain_core.tools import BaseTool

# LangGraph imports
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, create_react_agent

# MCP imports
from fastmcp import Client
from langchain_mcp_adapters.tools import load_mcp_tools

# --- 1. Define the Agent's State (The 'memory' of the graph) ---
# This is crucial in LangGraph. All data flows through this state.
class AgentState(TypedDict):
    # 'messages' is the core of the state, holding the conversation history
    # 'operator.add' tells LangGraph to APPEND new messages instead of overwriting
    messages: Annotated[List[BaseMessage], operator.add]
    
    # You can add other keys like 'current_tool_name' if needed

# --- 2. The Model Call Node (The 'Brain') ---
# This function is a node that calls the LLM.
# It uses the LLM we bound to the tools later (llm_with_tools).
def call_model(state: AgentState, llm) -> dict:
    # Get the conversation history from the state
    messages = state["messages"]
    # Invoke the LLM
    response = llm.invoke(messages)
    # The output is a dict that updates the state
    return {"messages": [response]}

# --- 3. The Routing Logic (The 'Decision Maker') ---
def should_continue(state: AgentState) -> str:
    """Decides whether to continue the loop."""
    last_message = state["messages"][-1]

    print(last_message.type)
    print(last_message)
    print(f"Content: {last_message.content}")

    # 1. Check if the LLM is requesting tool use.
    if isinstance(last_message, AIMessage) and last_message.tool_calls:
        return "tools"
    
    # 2. Check if the LLM provided a final answer (i.e., content exists).
    # This assumes the LLM has generated a response that is NOT a tool call.
    if last_message.content:
        return "end"
        
    # 3. Fallback/Error: If it's a ToolMessage or an empty AIMessage, loop back to the agent.
    # This shouldn't be necessary if the previous steps work, but acts as a safeguard.
    return "agent" # Or raise an error if you want strict termination.


async def talkToServer():
    print("Initializing LangGraph Agent...")
    model_name = "qwen3:1.7b" # Use a model with good tool-calling ability
    
    client = Client("http://localhost:8000/mcp")
    async with client:
        # Load tools from the MCP server
        tools: List[BaseTool] = await load_mcp_tools(client.session)
        print(f"Loaded tools: {[tool.name for tool in tools]}")
        
        # Instantiate the LLM
        llm = ChatOllama(model=model_name, temperature=0.1) 
        
        # Bind the tools to the LLM (crucial step for the LLM to know its tools)
        llm_with_tools = llm.bind_tools(tools)

        # --- 4. Define the Nodes and Edges (The State Machine) ---
        workflow = StateGraph(AgentState)

        # Node A: The LLM/Agent's thinking and action selection
        workflow.add_node("agent", lambda state: call_model(state, llm_with_tools))
        
        # Node B: The Tool Executor (LangGraph's pre-built handler)
        # This node handles parsing the tool call and running the function.
        workflow.add_node("tools", ToolNode(tools))

        # Set the entry point: Start by calling the agent
        workflow.set_entry_point("agent")

        # Add the conditional edge for routing
        # After the agent runs, call 'should_continue' to decide where to go
        workflow.add_conditional_edges(
            "agent",
            should_continue,
            {
                "tools": "tools", # If tool_calls exist, go to 'tools' node
                "end": END        # If no tool_calls, go to the 'END'
            },
        )

        # Add the return edge from the tools
        # After the tools run, they must go back to the agent to summarize the results
        workflow.add_edge("tools", "agent")

        # Compile the graph into a runnable
        app = workflow.compile()
        print("LangGraph Agent is ready.")

        # --- 5. Invoke the Graph ---
        user_input = "Please use the speak_it tool to say 'Welcome to LangGraph, it works!'"
        
        # The input is a dict with the initial message for the state
        final_state = await app.ainvoke({"messages": [HumanMessage(content=user_input)]})
        
        # The final answer is in the last message of the state's message list
        final_response = final_state["messages"][-1].content

        print("\n--- Final Agent Response ---")
        print(final_response)
        
if __name__ == "__main__":
    # You will need to install LangGraph: pip install langgraph
    asyncio.run(talkToServer())
