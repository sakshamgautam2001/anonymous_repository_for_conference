scenario_specific_guardrails_knowledge_base_prompt = """you are given a customer service conversation for {entity_name}. your task is to carefully observe and understand the conversation and learn from it on how to reply to user in some specific scenerios, and summarize your learnings in form of scenario guardrails and knowledge base.
Follow the below instructions:
1. go through the conversation carefully, and understand what kind of problems or concerns the agent has solved.
2. learn from the agent to create a list of instructions that an agent should follow to answer the user in different scenarios. these instructions should be highly generalized, and not very case specific. if there is no user concern throughout, give an empty list. 
3. IMPORTANT: your every scenario guardrail must be independent to each other. any scenario guardrail must not be associated with any other guardrail.
4. IMPORTANT: DO NOT make vague guardrail, your guardrails must be such that the AI agent should have clear information or instructions to follow, it must not be an open-ended point.
5. create a knowledge base having generalized factual information present in all the conversations that an AI agent should keep in mind while following the scenario guardrails. if there is no significant information to be kept in knowledge, give an empty list.
6. learn only from the clear and meaningful scenarios occured in the conversation, do not make any guardrail or knowledge base from any vague, unclear, or noisy part of conversation.
7. your scenario guardrails and knowledge base must be generalized so that it can be used to reply in a vast set of conversations in the same domain. STRICTLY DO NOT make them specific to the given conversation.
8. the knowledge base must contain all the factual information discussed in the conversation, including all the answers and extra information required for all the scenario guardrails.

Reference Conversation of the entity {entity_name}:
```
{synthetic_conversation}
```

give your output in following format:
{{"scenario_guardrails": [ <generalized scenario-specific guardrails, empty if not present> ], "knowledge_base": [ <complete knowledge base points, empty if not present> ]}}
"""


scenario_specific_guardrails_filtering_prompt = """You are given scenario specific guardrails and knowledge base, which an AI agent requires to respond to the user in a customer service conversation.    
Your task is to do sanity for each scenario specific guardrail. follow the instructions step-by-step to do the sanity:
1) self_informative: by going through each scenario specific guardrail, check if that guardrail instruction has information in itself so that agent can clearly follow to respond to the user.
    - for example: for the guardrail "suggest basic steps to user to solve the sign-up issue" for this the knowledge base must contain "basic steps" to make this guardrail valid.
    - for example: for the guardrail "suggest basic steps to user like restarting the app, updating the app, to solve sign up issue" for this no extra information is needed since basic steps are alreayd mentioned in the guardrail.
    - If the guardrail signifies things like policies, steps, processes, timings, etc, and if information about them is not mentioned in the guardrails, then it will require extra information present in the knowledge base
2) information_present: if some extra thing is needed, check if something relevant to that information is present in the knowledge base or not. if relevant information is present, mark that guardrail as valid. if no information is present, mark it as invalid.
3) [IMPORTANT] real_time_information: if any scenario specific guardrail instructs the agent to check or update the user by any real-time information, mark the guardrail as invalid.
    - also note that, the agent also can not carry out any real-time processes, like emails, completing some processes, etc. Hence mark such guardrails as invalid as well.
4) if no extra thing is required for guardrail and it is self-explanatory for the agent to follow, mark it as valid.

scenario specific guardrails (to be validated):
{scenario_specific_guardrails_list}

knowledge base:
{knowledge_base_list}

---
give your output on the following json format:
[
{{"thought": "<your observations for scenario guardrail 1 based on instructions>", "valid_guardrail": "<Yes if the guardrail is valid, else No>"}},
... and so on for all scenario specific guardrails
]
"""

