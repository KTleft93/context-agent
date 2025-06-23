from langchain.tools.retriever import create_retriever_tool

def get_pdf_tool(retriever):
    return create_retriever_tool(
        retriever=retriever,
        name="uploaded_pdf",
        description="Search and return data from the uploaded PDF."
    )
