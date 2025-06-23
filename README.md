# 🧠 PDF Chat Agent with Web Context

Chat with your PDFs and supercharge answers with live Google search context. This Streamlit-based app lets you upload a PDF and ask questions about its contents using a powerful LLM agent.

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b)
![LangChain](https://img.shields.io/badge/LangChain-Agent-green)

---

## 🚀 Features

- 📄 Upload any PDF and query its contents conversationally
- 🧠 Uses OpenAI's LLM with LangChain AgentExecutor
- 🔍 Real-time **Google Search Tool** for additional context
- ⚡ Fast vector-based document retrieval using **FAISS**
- 🌐 Web-based UI built with **Streamlit**

---

## 📦 Environment Setup

Use the included `environment.yml` file to get started quickly with `conda`.

```bash
conda env create -f environment.yml
conda activate file-chatbot

```

## 🔑 Configuration

You'll need an OpenAI API key to run this app.

Set your API key as an environment variable:

```bash
export OPENAI_API_KEY=your-key-here

```
🛠 How to Run

```bash
streamlit run script.py
```

## 🧩 Powered By

LangChain
Streamlit
OpenAI GPT
FAISS


## 🧪 Example Use Case

Upload a research paper.
Ask: "What is the author's main argument?"
Ask follow-up: "Can you find related studies online?"
The agent performs a Google search and combines it with the PDF context for enhanced answers.


## 📜 License

MIT License. See LICENSE file for details.




