import asyncio
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from mcp_use import MCPAgent, MCPClient
from file_agent import FileAgent

async def main():
    # Load environment variables
    load_dotenv()
    #Create configuration dictionary
    config = {
      "mcpServers": {
        "playwright": {
          "command": "npx",
          "args": ["@playwright/mcp@latest", "--caps" , "pdf", "--output-dir", "./output"],
          "env": {
            "DISPLAY": ":1"
          }
        }
      }
    }

    # Create MCPClient from configuration dictionary
    client = MCPClient.from_dict(config)

    # Create LLM
    #llm = ChatOllama(model="Model_Name", temperature=0.1, max_tokens=200)

    llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",  # This uses Gemini 1.5/2.5 depending on account
    temperature=0.7,
    top_p=1
    )

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=10, memory_enabled = True)

    # Read prompt from prompt.md file
    prompt_content = ""
    if os.path.exists("prompt.md"):
        with open("prompt.md", "r", encoding="utf-8") as f:
            prompt_content = f.read()
    else:
        print("Prompt file not found. Using default prompt.")
        prompt_content = """
        # Default prompt for MCP Agent
        This is a default prompt for the MCP Agent. Please provide a valid prompt file.
        """         
    # Run the query
    result = await agent.run(
        prompt_content
    )

    file_agent = FileAgent("output.html")
    file_agent.write_content(result)
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())
