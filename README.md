# Learning Path Generator (MCP Server)

An MCP (Model Context Protocol) server in Python that exposes a `generate_learning_path` tool. It creates a week-by-week learning plan for any topic, level and duration. The same core logic also powers a Streamlit web UI.

Built during an MCP workshop. The generator is template-based (fixed rules and a small resource list), not AI-generated.

## Project structure

    core.py            # learning path logic (shared)
    server.py          # MCP server (used by Cursor / Claude)
    app.py             # Streamlit UI
    requirements.txt

## Tool

`generate_learning_path(topic, level="beginner", weeks=4)`

- topic: e.g. python, machine learning, bioinformatics
- level: beginner, intermediate or advanced
- weeks: number of weeks in the plan

## Setup

    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt

## Run the Streamlit UI

    streamlit run app.py

## Connect the MCP server to Cursor

Create `.cursor/mcp.json` in your project folder, using your own paths:

    {
      "mcpServers": {
        "learning-path": {
          "command": "C:/path/to/project/venv/Scripts/python.exe",
          "args": ["C:/path/to/project/server.py"]
        }
      }
    }

Then open Cursor Settings, go to Tools and MCP, and turn on `learning-path`. In the agent chat, try:

    Use the learning-path tool to generate a 4 week learning path for bioinformatics at beginner level

Note: this project uses `mcp<2`, because `FastMCP` was renamed in mcp 2.x.

## Screenshots

See the `screenshots` folder: Cursor project folder, Streamlit input, Streamlit result, and the Cursor agent calling the MCP tool.
