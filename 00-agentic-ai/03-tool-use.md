[Course link](https://learn.deeplearning.ai/courses/agentic-ai/lesson/3s0czq/what-are-tools%3F)

## What are tools

- tools are code that the LLM can request to be executed
- LLMs use a range of tools and functions to gather information and execute tasks
- LLMs choose which tools to use depending on what is being asked (i.e. time, web search, image generation, db query)
- important to make sure your LLM has access to the appropriate tools and functions to complete a given task

## Tool creation

- Create the tool
- Provide it to the LLM
- Tell the LLM that it's available and how to use it

## Tool syntax

ex:

```python
from datetime import datetime

def get_current_time():
    """Returns the current time as a string"""
    return datetime.now().strftime("%H:%M:%S")

###################

import aisuite as ai
client = ai.Client()

response = client.chat.completions.create(
    model = "openai:gpt-4-o",
    messages = messages,
    tools = [get_current_time],
    max_turns = 5
)
```

- max-turns = maximum number of tool cals before finishing the task (LLM may decide to continue calling follow-up tasks, this limits that.)
- under the hood (or explicitly in some cases), a JSON is generated to list all tools, with name, description and parameters described in a uniform format
- code execution tool is especially powerful

## Good tool design

- Keep tool docstrings short, imperative, and specific to the action.
- Return consistent, compact JSON so the model can chain results.
- Prefer one clear responsibility per tool (single route, single effect).
- When asking an LLM to use tools, give it a clean, clear prompt wrapper so it understands its role, permission to use tools, and understands when to execute actions directly vs. when to ask for human permission. This wrapper will be a preable for all prompts related to given tool use. ex:

```txt
# build prompt / wrapper
- You are an AI assistant specialized in managing emails.
- You can perform various actions such as listing, searching, filtering, and manipulating emails.
- Use the provided tools to interact with the email system.
- Never ask the user for confirmation before performing an action.
- If needed, my email address is "you@email.com" so you can use it to send emails or perform actions related to my account.

# action prompt
Delete the Happy Hour email

```

## Code execution

- enables LLM to write custom code to solve the user's request
- best practice is to run code execution tasks inside a sandbox

## MCP

- Model Context Protocol
- Created by Anthropic, now widely adopted.
- new protocol to develop LLM-based applications -new way to give LLMs access to more context and more tools
- many teams were independently creating custom tools to integrate with different services (think Slack, GDrive etc.), resulting in a lot of duplicate work. MCP proposed a uniform standard for tool access so that data connection needed to be crated jut once and could then be reused by different teams
- client / server structure:
  - clients are the AI tools/apps/LLMs that want access to services (i.e. Cursor, Claude, Windsurf)
  - servers are the tools/apps being called (ex: GitHub, PostgreSQL, Slack, Google)
