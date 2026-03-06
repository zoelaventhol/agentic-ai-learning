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

## Code execution

- enables LLM to write custom code to solve the user's request
