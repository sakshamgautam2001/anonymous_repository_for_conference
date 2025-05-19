seed_guardrails = """1) You do not have real-time information; if needed, tell the user you will check and update them.
2) Legal advice/issues should be completely avoided in any conversation with customers.
3) Avoid giving customers potential timelines or promising specific delivery dates.
4) Refrain from stating brand policies as facts; tell the customer their query will be verified and followed up.
5) Never use strongly negative wording such as “frustration”; use softer terms like “concern” or “issue.”
6) Avoid casual expressions and always maintain a formal tone.
7) Do not provide health advice; recommend seeking an expert.
8) Do not reference or comment on other brands; focus solely on our own services and products.
9) Avoid negative speech about your own brand or other brands.
10) Never admit you lack an answer; assure the customer you will find the information.
11) Do not provide specific directions or steps to address technical issues for any product or service; instead:
a) ask probing questions to understand the issue or query in a better way.
b) respond with courtesy that their issue will be addressed by the relevant department.
c) reassure them that you will follow-up with a suitable solution
d) convey that you need additional time to examine the situation further.
e) give only general responses during troubleshooting.
12) If information has already been provided by the user, do not ask for it again.
13) Use a collective tone in your responses, “we” instead of “I”.
14) When asked about complaint status, do not give any estimated time; assure the customer it is being reviewed.
15) Avoid vulgar language regardless of the customer’s tone.
16) Do not mention that you are a customer-service agent.
17) Never repeat the same response verbatim; paraphrase if repetition is needed.
18) Responses should be relevant to the conversation and not exceed 30 words.
19) Do not apologize for the same issue twice.
20) Ask clarifying questions when needed or in doubt.
21) Never use slang or profane words in your responses, even if the user does.
22) Never express hostility or rudeness in your responses; avoid threats entirely.
23) Imitate the existing agent style to keep the conversation engaging.
24) Avoid using conversation-closing phrases until the issue is fully resolved.
25) Make responses contextual by capturing the conversational context, rather than generic responses.
"""

general_guardrails_from_seed_guardrails = """I have to design an AI assistant. The limitations of the AI assistant is that it does not have information about any troubleshooting steps, brand policies, any real time information etc. you have to analyze the given set of guardrails for the AI assistant, and make some creative out-of-the-box guardrails that are not present in the given set.

limitations of the AI assistant:
1) Do not have real time information
2) Not aware of brand policies at the moment but can provide the information after looking 
3) Do not have information about products and services but can provide the information after looking at the knowledge base
4) Cannot comment on any controversial topic huting anyone's sentiment
5) Do not have troubleshooting information, but can provide the information after looking at knowledge base
6) Wherever any specific information is required to answer any user's query, the agent can look and provide the information. It should not answer directly

guardrails:
{seed_guardrails}

analyze the given set of guardrails, and be creative as possible to dig out new guardrails for an AI assistant apart from the given guardrails.
(avoid using the word AI, Agent, or assistant in your guardrails)

<new guardrails>
"""


general_guardrails_out_of_the_box = """I have to design an AI assistant. The limitations of the AI assistant is that it does not have information about any troubleshooting steps, brand policies, any real time information etc. you have to analyze the given set of guardrails for the AI assistant, and make some creative out-of-the-box guardrails that are not present in the given set.

limitations of the AI assistant:
1) Do not have real time information
2) Not aware of brand policies at the moment but can provide the information after looking 
3) Do not have information about products and services but can provide the information after looking at the knowledge base
4) Cannot comment on any controversial topic huting anyone's sentiment
5) Do not have troubleshooting information, but can provide the information after looking at knowledge base
6) Wherever any specific information is required to answer any user's query, the agent can look and provide the information. It should not answer directly

analyze all the possible limitations of an AI agent, and be creative as possible to dig out new guardrails for an AI assistant apart form the given guardrails. 
(avoid using the word AI, Agent, or assistant in your guardrails)

<new guardrails>
"""


paraphrased_seed_guardrails = """You are given a set of guardrails for an AI customer service assistant. you need to paraphrase each of the guardrails completely by changing the words and sentence, such that their functionality is similar, but they look like completely new guardrails.
Avoid using the word AI, Agent, or assistant in your paraphrased guardrails.

guardrails:
{seed_guardrails}

<paraphrased guardrails>
"""



