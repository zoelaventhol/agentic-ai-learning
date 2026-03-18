[Course link](https://learn.deeplearning.ai/courses/agentic-ai/lesson/jcl177/planning-workflows)

## Planning workflows

- for complex workflows, the LLM should decompose a prompt into a series of sequential steps. Usually the agent can do this independently.
- this is built in to many coding assistant workflows.

## Creating and executing LLM plans

- get an LLM to create a plan in JSON - this can help with later stages of the workflow. (ex: {step: 1, task: "example"} )
- md and txt are less reliable
- can also plan with code execution:
  - custom-creating tools to allow LLMs to execute any imaginable query quickly gets inefficient.
  - allowing the LLM to write and execute its own code to solve a problem gives it infinitely more capability (under the hood, it has access to all existing python, pandas etc libraries).
- drawback is that is the LLM is independently planning and executing, it gives the developer less insight as to what it will produce at runtime.
