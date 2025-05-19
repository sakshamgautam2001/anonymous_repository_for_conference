response_quality_prompt = """You are given a set of KPI Instructions, the system prompt on which AI agent is working, conversation ending with user messages, and generated AI agent response. you need to evaluate the quality of AI agent response based on the following KPIs:

1. Contextual: The response should be logical and coherent (even if not answering the user question), both within its own context and also within the broader conversation. It should maintain the context and make sense in the flow of conversation.
2. Relevancy: the response should be relevant to what user has asked in conversation, providing an appropriate response. even if agent response do not contain answer (as per the system prompt), it should be a relevant response to the user query.
3. Structure: the way response is written must look like it is written by an expert, and must not look naive. the response must have a fluent and smooth flow while reading, and easy to read for a user. Check for every scope of structure improvement in this.
4. Usability: The response should be specific enough to provide valuable and to-the-point information required. It should neither contain too broad or irrelevant information which is not required or requested by the user, nor too vague information, and should only contain useful and required information needed to reply to the user.
5. Tonality: the generated response should be in similar tone of the agent replies in the conversation, and should be consistent with the tone.

IMPORTANT Instructions while evaluating:
- You have a full access of AI agent system prompt which must be adhered to generate the AI agent response to reply the user. Make sure your evaluation reasoning must not contradict the guardrails, instructions, or knowledge base present in the AI agent system prompt.
- If AI agent response is lacking in any of the KPI because it has lack of information and required information is not available in its system prompt, then do not cut rating in such cases, because information is limited and it can not provide details outside its system prompt, leading to hallucination. If the required information is present in system prompt that AI response has not provided, then only cut the rating.
- If AI agent response is lacking in any of the KPI just because it has to adhere to certain guardrials (in its system prompt) properly, then do not cut the rating in such cases. DO NOT contradict with the AI agent system prompt.

---
Given below is the AI agent system prompt:
```
{system_prompt}
```

Given below is a conversation between the User and Agent.
conversation:
{customer_service_conversation}

AI agent response (to evaluate): {response}

---
Your output must be in the following processable json format:
```
[
    {{ "Contextual": <contextual_score>, "reason": "<reasoning for the contextual_score based on Contextual KPI>" }},
    {{ "Relevancy": <relevancy_score>, "reason": "<reasoning for the relevancy_score based on Relevancy KPI>" }},
    {{ "Structure": <structure_score>,"reason": "<reasoning for the structure_score based on Structure KPI>"  }},
    {{ "Usability": <usability_score>, "reason": "<reasoning for the usability_score based on Usability KPI>" }},
    {{ "Tonality": <tonality_score>, "reason": "<reasoning for the tonality_score based on Tonality KPI>" }}
]
```

Evaluate: Do hard evaluation of generated agent response. if the agent response even slightly lacks in any of the KPIs as per their defination, cut the rating accordingly, keeping the given IMPORTANT Instructions and without contradicting with AI agent system prompt. If it fully satisfies, then only give full rating.
Rate: Assign categories based on these values: 1 for very low, 2 for low, 3 for medium, 4 for high, and 5 for very high.
Reason: Give a valid reasoning based on your thought why you gave the respective score to the agent response, without contradicting with AI agent system prompt, and considering the IMPORTANT Instructions given.
"""