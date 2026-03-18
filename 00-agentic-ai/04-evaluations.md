[Course link](<https://learn.deeplearning.ai/courses/agentic-ai/lesson/pu5xbl/evaluations-(evals)>)

## What are Evaluations

- effective evaluation are what sets apart a really good AI system
- note patterns in mistakes to target them better
- good quick process for evals:
  1. Build a system and look at outputs to see where mistakes are happening or improevments are needed
  2. Put a small eval in place with limited sample size to help trakc progress
  3. Monitor this eval as you make changes to the workflow (i.e. prompt updates, algorithm changes etc. to see if the identified issues improve)
- Components of a good eval:
  1. Binary or concrete criteria (i.e. did A happen? is B true? was X, Y, Z mentioned?)
  2. Translate these binary outcomes to a score
- end-to-end evals plus evals for specific phases of the workflow

## Error analysis and prioritizaiton

- focus on the examples where system is NOT performing well (successfull examples don't need more work)
- look at trace of full process - understand which component of the process is creating the error

## Latency and cost optimization

- First priority is a high-functioning system
- After that, cost optimization and latency might become important focuses
- Consider parallelism, smaller steps with smaller models, or faster LLM providers
- Costs can be driven by:
  - LLM steps (per-token)
  - API tools calls (per API call)
  - compute steps (server capacity/cost)
- break down each step to analyze cost and latency, and adapt each step accordingly
