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

## Multi-agentic workflows

- breaking down a task into subtasks
- think about how a human team would work: different skill sets needed (ex: research, design, writing, editing, management); and what tasks you would delegate to each and what tools they may need
- create linear workflow - ex: research -> design -> writing -> editing -> QA
- whereas before we might have given an LLM access to a suite of tools, now we might give a "leading" LLM access to a "team" of specialized agents.

## Communication patterns for multi-agent systems

- linear: sequentially pass a task to a series of agents
- hierarchical: "manager" LLM passes tasks to "team" of agents, reviews each output and delegates to another agent as needed
  - can have multiple levels with multiple mid-managers for subtasks - less common but possible
- all-to-all: tell all agents on the team about each other and let them know they can call on each other as needed
  - in practice can be a bit less reliable outputs
