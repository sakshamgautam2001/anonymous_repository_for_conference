hallucination_eval_prompt_1 = """You are given a conversation between agent and user, and the agent response as a reply to the conversation that you need to evaluate on hallucination.
You are also given the guardrails that the agent has to follow while responding, conversational context, and the entity description as the available information, any information used in response outside this given information in any form will be a hallucinated information.
Follow the below instructions to check the hallucinated information:
1. carefully go through the customer service conversation, entity description, and guardrails to consume every bit of available information that an agent can use.
2. now observe the agent response to reply in conversation, and check every information present in it about if it is based on the available information that agent have.
3. If you have found any kind of information used in response in any form, whether is a fact, process, or a question asked by agent to user, which is not backed or instructed by the given information anywhere, mark it as hallucinated.
4. note that the information provided in agent response should be on the basis of the available information, if agent has provided any information which is not present even if it is quite obvious information (such as a defination, description of anything, or any process), mark it as hallucinated.
5. Any kind of link or resource provided in agent response, which is not exactly mentioned anywhere in available information, is a hallucinated information.
6. If the agent is asking something to the user which is not instructed anywhere to ask in the available information, then it is a hallucinated information.
7. If the Agent response has shown a completion of a task that requires real-time access, mark it as a hallucination.
8. Following scenarios will not be counted in hallucination:
    - If the agent makes general statements without including any information, they are not counted in hallucination.
    - If agent does not have available information or access to provide the answer to user, then Agent response can deny about it or show unavailability in its response as an answer, and this will not be counted in hallucination, even if it is not mentioned anywhere.

entity name: {entity_name}
entity description: {entity_description}

guardrails:
{general_guardrails_list}

conversation:
{customer_service_conversation}

Agent response (to evaluate): 
{response}

---
give your output on the following processable json format only:
{"hallucinated_information": [<list of all the hallucinated information present in Agent response, empty list if no hallucination>], "hallucination": "<Yes or No>"}
"""




hallucination_eval_prompt_2 = """You are given a conversation between agent and user, and the agent response as a reply to the conversation that you need to evaluate on hallucination.
You are also given the guardrails, entity guidelines, and knowledge base that the agent has to follow while responding, conversational context, and the entity description as the available information, any information used in response outside this given information in any form will be a hallucinated information.
Follow the below instructions to check the hallucinated information:
1. carefully go through the customer service conversation, entity description, entity guidelines and knowledge base, and guardrails to consume every bit of available information that an agent can use.
2. now observe the agent response to reply in conversation, and check every information present in it about if it is based on the available information that agent have.
3. If you have found any kind of information used in response in any form, whether is a fact, process, or a question asked by agent to user, which is not backed or instructed by the given information anywhere, mark it as hallucinated.
4. note that the information provided in agent response should be on the basis of the available information, if agent has provided any information which is not present even if it is quite obvious information (such as a defination, description of anything, or any process), mark it as hallucinated.
5. Any kind of link or resource provided in agent response, which is not exactly mentioned anywhere in available information, is a hallucinated information.
6. If the agent is asking something to the user which is not instructed anywhere to ask in the available information, then it is a hallucinated information.
7. If the Agent response has shown a completion of a task that requires real-time access, mark it as a hallucination.
8. Following scenarios will not be counted in hallucination:
    - If the agent makes general statements without including any information, they are not counted in hallucination.
    - If agent does not have available information or access to provide the answer to user, then Agent response can deny about it or show unavailability in its response as an answer, and this will not be counted in hallucination, even if it is not mentioned anywhere.

entity name: {entity_name}
entity description: {entity_description}

general guardrails:
{general_guardrails_list}

scenario specific guardrails:
{scenario_specific_guardrails_list}

knowledge base: 
{knowledge_base_list}

conversation:
{customer_service_conversation}

Agent response (to evaluate): 
{response}

---
give your output in the following processable json format only:
{{"hallucinated_information": [<list of all the hallucinated information present in Agent response, empty list if no hallucination>], "hallucination": "<Yes or No>"}}
"""