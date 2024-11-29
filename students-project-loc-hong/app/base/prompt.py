from base.const import (
    INPUT_LANGUAGE_KEY,
    VAR_DOCUMENT_KEY,
    INPUT_NWORDS_KEY,
    VAR_EXISTING_SUMMARY_KEY,
)

INPUT_QUESTION_KEY = "question"

STUFF_GOAL_MESSAGE = """
Your task is to answer a question posed by a human using the information provided in the Context.
""".lstrip().rstrip()

ANSWERING_RULES_MESSAGE = f"""
In crafting your response, you MUST adhere to the following 8 rules:
1. Use Provided Context: Your answer MUST utilize the information provided in the Context.
2. Supplement with General Knowledge: You may supplement your answer with relevant details drawn from your general knowledge ONLY IF the primary information comes from the Context.
3. Never Guess: If it is not possible to craft a response with clear refereces to the information sourced from the Context then do not make guesses and ask the human to provide more context or details that may help.
4. Clarify Ambiguities: If the question is ambiguous or the context allows for multiple possible answers then list the possible interpretations and ask the human to specify which one applies so you can provide a more accurate answer.
5. Specify Conditional Information: Clearly state in your response if any piece of information used from the Context is subject to specific conditions such as applicability of laws, rules, or other contingent factors.
6. Format Your Response: Your response must be formatted as follows:
- Answer: [Your Answer]
- Information: [List bullet points with the information used to answer the question]
- References: [List sources used to answer the question, including page numbers if available]
7. Contextual Relevance: Clearly indicate if your response does not rely on information in the provided Context.
8. Language Requirement: Respond in the specified language: {{{INPUT_LANGUAGE_KEY}}}.
""".lstrip().rstrip()

MAX_LENGTH_MESSAGE = f"""
Your response must not exceed the length of {{{INPUT_NWORDS_KEY}}} words.
""".lstrip().rstrip()

CONTEXT_MESSAGE = f"""
Here is the Context for the Question, enclosed between Triple Single Quotes:
'''
{{{VAR_DOCUMENT_KEY}}}
'''
"""

REFINE_GOAL_MESSAGE = """
Your task is to answer a question posed by a human, using the information given in the context provided. To manage the length, the context has been divided into segments, which are being analyzes iteratively one after one.
"""

REFINE_MESSAGE = """
Based on earlier segments, a temporary answer has already been formulated. You now have the opportunity to revise that temporary answer completely in light of an additional context segment or to refine it by incorporating new information and thus improve accuracy, clarity, and completeness. If the new segment does not add relevant information for the sake of the question then skip it and retain the original answer.
"""

TEMP_ANSWER_MESSAGE = f"""
Here is the Temporary Answer, enclosed between Triple Single Quotes:
'''
{{{VAR_EXISTING_SUMMARY_KEY}}}
'''
"""

FIRST_CONTEXT_ANSWER_MESSAGE = f"""
Here is the First Context Segment, enclosed between Triple Single Quotes:
'''
{{{VAR_DOCUMENT_KEY}}}
'''
"""

ADDITIONAL_CONTEXT_ANSWER_MESSAGE = f"""
Here is the Additional Context Segment, enclosed between Triple Single Quotes:
'''
{{{VAR_DOCUMENT_KEY}}}
'''
"""

PROMPT_TEMPLATE_INITIAL_SUMMARY = [
    ("system", REFINE_GOAL_MESSAGE),
    ("system", ANSWERING_RULES_MESSAGE),
    ("system", FIRST_CONTEXT_ANSWER_MESSAGE),
    ("system", MAX_LENGTH_MESSAGE),
    ("human", f"{{{INPUT_QUESTION_KEY}}}"),
]

PROMPT_TEMPLATE_REFINE = [
    ("system", REFINE_GOAL_MESSAGE),
    ("system", REFINE_MESSAGE),
    ("system", ANSWERING_RULES_MESSAGE),
    ("system", TEMP_ANSWER_MESSAGE),
    ("system", ADDITIONAL_CONTEXT_ANSWER_MESSAGE),
    ("system", MAX_LENGTH_MESSAGE),
    ("human", f"{{{INPUT_QUESTION_KEY}}}"),
]

PROMPT_TEMPLATE_STUFF = [
    ("system", STUFF_GOAL_MESSAGE),
    ("system", ANSWERING_RULES_MESSAGE),
    ("system", CONTEXT_MESSAGE),
    ("system", MAX_LENGTH_MESSAGE),
    ("human", f"{{{INPUT_QUESTION_KEY}}}"),
]
