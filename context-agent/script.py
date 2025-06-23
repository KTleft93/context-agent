import streamlit as st
import tempfile
from dotenv import load_dotenv

from loaders.file_loader import load_and_split_pdf
from vectorstore.faiss_store import create_faiss_vector_store
from tools.retrieval_tool import get_pdf_tool
from tools.search_tool import get_search_tool
from prompts.custom_prompt import get_custom_prompt
from agents.agent_executor import create_agent
load_dotenv()

st.set_page_config(page_title="File Chat", layout="wide")
st.title("📄 Chat with Your File Upload")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        pdf_path = tmp_file.name

    docs = load_and_split_pdf(pdf_path)
    retriever = create_faiss_vector_store(docs)

    pdf_tool = get_pdf_tool(retriever)
    search_tool = get_search_tool()
    tools = [pdf_tool, search_tool]

    prompt = get_custom_prompt()
    agent_executor = create_agent(tools, prompt)

    user_input = st.text_input("Ask a question about the PDF:")
    if user_input:
        with st.spinner("Thinking..."):
            try:
                response = agent_executor.invoke({"input": user_input})
                st.markdown(f"**Bot:** {response['output']}")
            except Exception as e:
                st.error(f"❌ Error: {e}")


