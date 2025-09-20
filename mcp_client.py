import asyncio

from fastmcp import Client

client = Client("http://localhost:8000/mcp")

async def main():
    async with client:
        tools = await client.list_tools()
        print(tools)
        # ok we know we have a tool called speak_it that takes content
        result = await client.call_tool("speak_it", {"content":"Test content over the wire"})
        result = await client.call_tool("speak_it", {"content":"Yes sir"})
        result = await client.call_tool("speak_it", {"content":"No sir"})
        result = await client.call_tool("speak_it", {"content":"[MAN] cough"})
        print(result) 



asyncio.run(main())
