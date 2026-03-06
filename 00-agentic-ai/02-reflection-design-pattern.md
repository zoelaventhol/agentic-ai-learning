[Course link](https://learn.deeplearning.ai/courses/agentic-ai/lesson/shknq1/reflection-to-improve-outputs-of-a-task)

## What is Reflection Design Pattern

- task -> output -> reflect or revise -> final output
- ex: write a draft essay, review, make a final draft OR write code, review for bugs, revise.
- works best with external input where possible: i.e. run the code and provide error output
- direct generation / zero-shot prompting: direct prompt without much context or examples
- multi-shot prompting: prompt with multiple examples
- reflection prompt: a separate prompt guiding the agent to review something specific about the original output
- create a dataset of prompts and answers: pipeline of review steps
- play with different models: some have different strengths (ex: reasoning models often better at review/reflection)

## Evaluating the impact of reflection

- think about building evals when you try out different prompts: evaluate which setup/prompt gives you better outputs. in cases where there is a concrete correct or incorrect answer, you can evaluate based on this. in more subjective or less concrete cases, you can use another LLM to evaluate/judge.
  - however, need to be careful about this to get good results - open-ended questions like "which is better" usually don't give good results
  - many LLMs have a position bias to prefer the first option given
  - for best results: create a rubric made up of binary evaluations. i.e. for evaluating chart quality: has clear title; axis labels present and clear; appropriate chart type; appropriate range
- so for objective, black-and-white, correct/incorrect evals: code-based eval is okay. good to include dataset of examples
- for more subjective evals: use LLM as a judge, with a clearly defined rubric

## Using external feedback

- best performance is prompting + reflection + external feedback
- external feedback can include: error output, web search results, data set, etc.
