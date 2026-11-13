# Information Retrieval System — PDF Question Answering with RAG

## 📌 Overview

Information Retrieval System is an AI-powered application that allows users to interact with PDF documents by asking questions in natural language.

The application uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from uploaded documents and generate contextual answers using Google's Gemini models.

Built with Python, Streamlit, LangChain, FAISS, and Google Gemini, this project demonstrates how Large Language Models (LLMs) can be combined with document retrieval to build a practical question-answering system.

## ✨ Features

- **PDF Upload:** Upload one or multiple PDF documents.
- **Text Extraction:** Extract textual content from PDF files.
- **Text Chunking:** Split extracted text into smaller, overlapping chunks.
- **Text Embeddings:** Convert text chunks into numerical vector representations.
- **Vector Search:** Store and retrieve relevant chunks using FAISS.
- **AI-Powered Question Answering:** Generate answers using Google Gemini.
- **Conversational Memory:** Maintain conversation history during a session.
- **Interactive Interface:** Use a simple web interface built with Streamlit.

## 🏗️ Architecture

The application follows a Retrieval-Augmented Generation (RAG) pipeline.

1. The user uploads PDF documents.
2. The application extracts their text.
3. The text is divided into chunks.
4. Google Gemini embeddings convert the chunks into vectors.
5. FAISS stores the vectors and enables similarity search.
6. The user submits a question.
7. The retriever finds relevant document chunks.
8. Gemini generates an answer based on the retrieved context.
9. The answer is displayed in the Streamlit interface.

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web interface |
| LangChain | RAG pipeline and LLM integration |
| Google Gemini API | Text embeddings and answer generation |
| FAISS | Vector storage and similarity search |
| PyPDF2 | PDF text extraction |
| python-dotenv | Environment variable management |

## 📂 Project Structure

```text
Information-Retrieval/
│
├── app.py                  # Streamlit application
├── requirements.txt        # Python dependencies
├── setup.py                # Package configuration
├── template.py             # Project template or setup helper
├── test.py                 # Tests and experiments
├── .gitignore              # Files excluded from Git
│
├── research/
│   └── trials.ipynb         # Research and experimentation notebook
│
└── src/
    ├── __init__.py
    └── helper.py            # PDF processing, embeddings,
                             # FAISS and conversational chain
```

## ⚙️ Installation

### Prerequisites

- Python 3.10 or a compatible newer version
- A Google AI Studio API key
- Git

### 1. Clone the repository

```bash
git clone https://github.com/NajLaBm/Information-Retrieval.git
cd Information-Retrieval
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root:

```text
GOOGLE_API_KEY=your_google_api_key
```

Replace the placeholder with your own API key.

**Security:** Never commit `.env` or expose your API key in source code, notebooks, screenshots, or public repositories. Ensure `.env` is listed in `.gitignore`.

### 5. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## 🚀 How to Use

1. Launch the application.
2. Upload one or more PDF files using the sidebar.
3. Click **Submit & Process**.
4. Wait for the documents to be processed and indexed.
5. Enter a question in the question field.
6. Read the AI-generated answer based on the available document content.

## 🔎 How RAG Works

RAG combines two components:

- **Retrieval:** FAISS searches for document chunks relevant to the user's question.
- **Generation:** Gemini uses the retrieved context to formulate a natural-language answer.

This approach helps ground responses in the uploaded documents instead of relying exclusively on the model's general knowledge.

## ⚠️ Limitations

- Answer generation and embeddings depend on API availability and configured quotas.
- API usage may be subject to rate limits and provider policies.
- Scanned PDFs may require OCR if they do not contain extractable text.
- The quality of answers depends on document quality, chunking, retrieval settings, and the language model.
- The current application is designed as a local prototype; production deployment would require additional security, monitoring, and error handling.

## 🔮 Future Improvements

- Display the source documents and page references supporting each answer.
- Add OCR support for scanned PDF documents.
- Improve document retrieval using metadata filtering and reranking.
- Add persistent vector storage.
- Implement a more robust conversation interface.
- Support local LLMs through Ollama to reduce dependence on external generation APIs.
- Add automated tests and deployment configuration.

## 👩‍💻 Author

**Najia Ben Mahmoud**

Computer Science Engineer | Artificial Intelligence | Data Science | Business Intelligence

- GitHub: [NajLaBm](https://github.com/NajLaBm)
- Portfolio: [najia-benmahmoud.netlify.app](https://najia-benmahmoud.netlify.app)

---

*This project was developed to explore document retrieval, vector databases, embeddings, and LLM-based question answering using the RAG architecture.*
