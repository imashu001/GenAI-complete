# requirements: mcp
from mcp.server import Server
from mcp.server.stdio import stdio_server
import mcp.types as types

# Initialize the MCP server
app = Server("course-demo-server")

# 1. Expose a Resource (Read data)
@app.list_resources()
async def list_resources() -> list[types.Resource]:
    return [
        types.Resource(
            uri="course://syllabus/overview",
            name="GenAI Course Syllabus",
            mimeType="text/markdown",
            description="Overview of the Generative AI curriculum modules."
        )
    ]

@app.read_resource()
async def read_resource(uri: str) -> str:
    if uri == "course://syllabus/overview":
        return "# GenAI Curriculum\n1. Foundations\n2. RAG\n3. Agents\n...\n07. Model Context Protocol"
    raise ValueError(f"Resource not found: {uri}")

# 2. Expose a Tool (Executable action)
@app.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="calculate_module_duration",
            description="Calculate total estimated hours for course modules.",
            inputSchema={
                "type": "object",
                "properties": {
                    "num_modules": {"type": "integer", "description": "Number of modules in the course"}
                },
                "required": ["num_modules"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    if name == "calculate_module_duration":
        num_modules = arguments.get("num_modules", 1)
        total_hours = num_modules * 4.5  # 4.5 hours per module
        return [types.TextContent(type="text", text=f"Total estimated course duration is {total_hours} hours.")]
    raise ValueError(f"Tool not found: {name}")

# Run the server via stdio transport
async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())