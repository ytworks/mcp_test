# server.py
from mcp.server.fastmcp import FastMCP
import uuid


# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

@mcp.tool()
def gen_uuidv4():
    return str(uuid.uuid4())

if __name__ == "__main__":
    mcp.run()