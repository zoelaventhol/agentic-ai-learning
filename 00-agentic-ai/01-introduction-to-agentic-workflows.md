[Course link](https://learn.deeplearning.ai/courses/agentic-ai/lesson/nae3i1/what-is-agentic-ai)

## Agentic AI workflow & use cases

- agentic AI workflow: process where an LLM-based app executes multiple steps to complete a task
- most important is to be able to break down any task into discrete steps. for example, to write an essay: research, then secondary research, then synthesize, then draft, then refine etc.
- some systems are less autonomous, some more - i.e. less autonomous means follows a preset of instructions, more means it delegates multiple layers of decisionmaking. higher autonomy can still lead to a bit more unpredictability
- even lower-level LLMs can produce MUCH better results when utilized within an agentic workflow.
- key benefits: better performance, parallelization of workflows - means faster systhesis than humans, modular - can add, update or swap out tools to improve output in an existing flow
- computer use agents are growing - still emerging, still face some challenging parsing complex websites etc but will be huge once more stable
- agentic ai solutions are best-suited to tasks which:
  - have clear step-by-step process
  - standard procedures to follow
  - text assets only
- they can be used for, but it's more complex for tasks where:
  - steps are not known in advance
  - need to plan & solve as you go
  - require multimedia interactions (sound, image, video etc.)

## Task decomposition

- ex: writing an essay:
  1. write an outline on a topic
  2. web research
  3. write first draft
  4. review
  5. revise
- ex: respond to customer inquiry
  1. extract key info (what did customer ask?)
  2. find relevant information in system
  3. write response
  4. make sure tone and branding are consistent
- main building blocks of agentic ai flows:
  - models: LLMs (text generation, tool use, information extraction); specialized models (text-to-speech, image analysis etc.)
  - tools: APIs, information retrieval (dbs, RAG), code execution
- always ask yourself: can this task be implemented with an LLM or tool? if not, can i decompose it into tasks that can?

## Evaluating agentic workflows

- disciplined eval workflows are often what set apart a good agentic ai system
- manually look for low-quality output, and define patterns of what this is (i.e. theme of incorrect or undesired information?). can write checks for how often this defined undesired output happens
- can use LLM as a judge of output - i.e. ask it to rate agent output based on quality - can define rubric etc.
- two major types of evals:
  1. end-to-end evals - evaluates output quality of entire end-to-end process
  2. component-level evals - evaluates quality of specific tasks
- examine traces to perform error analysis - check output of each step in a wrokflow for errors or improvements

## Agentic design patterns

1. Reflection - process to identify and correct problems during implementation of a task. this could be completed by having one agent tasked with reviewing and improving its own work, or by splitting into 2 roles: for example, an implementer and a reviewer.
2. Tool use - for example: web research, code execution, image reading or generation
3. Planning - LLM needs to decomopose and identify the steps needed to complete a task, then executes
4. Multi-agent collaboration - mutliple agents each with a distinct role (ex: designer, coder, QA, documentation) - can be more unpredictable, but with refinement much more powerful
