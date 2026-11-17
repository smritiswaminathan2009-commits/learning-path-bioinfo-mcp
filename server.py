from mcp.server.fastmcp import FastMCP
from core import generate_path

mcp = FastMCP("learning-path-generator")

@mcp.tool()
def generate_learning_path(topic: str, level: str = "beginner", weeks: int = 4) -> dict:
    """Create a week-by-week learning path for any topic."""
    return generate_path(topic, level, weeks)

if __name__ == "__main__":
    mcp.run()
