from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import AzureChatOpenAI


from base.prompt import PROMPT_TEMPLATE_REFINE


prompt_const = [prompt[1] for prompt in PROMPT_TEMPLATE_REFINE]
prompt = PromptTemplate.from_template(".".join(prompt_const))


llm = AzureChatOpenAI(model="gpt-35-turbo")


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def get_answer_direct_from_llm(question):
    return llm.invoke(question)


def get_no_word(*args, **kwargs):
    return "100"


def get_language(*args, **kwargs):
    return "english"


def get_rag(retriever):
    rag_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough(),
            "existing_answer": get_answer_direct_from_llm,
            "n_word": get_no_word,
            "language": get_language,
        }
        | prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain
