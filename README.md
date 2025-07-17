# Automation Testing Framework

This project is an automated testing framework that uses Playwright with Model Context Protocol (MCP) and integrates with AI models for test execution. The framework reads test scenarios from a prompt file and executes them using Playwright automation.

## Features

- Playwright-based web automation testing
- Integration with AI models (Google's Gemini or Ollama)
- Prompt-driven test execution
- HTML report generation

## Prerequisites

- Python 3.x
- Node.js and npm (for Playwright)
- Google API Key (for Gemini) or Ollama setup

## Installation

1. Clone the repository
2. Install the required Python packages:
```bash
pip install langchain-google-genai python-dotenv langchain-ollama
```
3. Install Playwright MCP:
```bash
npm install @playwright/mcp
```

## Configuration

1. Create a `.env` file in the project root
2. Add your Google API Key:
```
GOOGLE_API_KEY=<YOUR_GOOGLE_API_KEY>
```

## Project Structure

- `mcp_agent.py` - Main script that handles test execution and AI integration
- `file_agent.py` - Handles file operations for report generation
- `prompt.md` - Contains test scenarios and instructions
- `output.html` - Generated test report

## Usage

1. Create or modify test scenarios in `prompt.md` following the format:
```markdown
Website: [URL]

Steps:
1. [Step Description]
    - Expect: [Expected Outcome]
2. [Step Description]
    - Expect: [Expected Outcome]
...
```

2. Run the automation:
```bash
python mcp_agent.py
```

## Report Format

The framework generates an HTML report containing:
- Test case details
- Pass/Fail status
- Expected outcomes
- Step-by-step results

## Example

The default example includes a YouTube search automation test that:
1. Navigates to YouTube
2. Searches for a specific term
3. Verifies search results
4. Generates an HTML report

## Contributing

Feel free to submit issues and enhancement requests.
