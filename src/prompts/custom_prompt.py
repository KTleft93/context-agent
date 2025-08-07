from langchain.prompts import PromptTemplate

def get_custom_prompt():
    return PromptTemplate.from_template("""
    You are an expert on the uploaded PDF content.
    You will answer user questions based on the PDF. If you do not know the answer, use Google search.

    Chat History:
    {chat_history}

    User Question:
    {input}

    Your Answer:
    """)
