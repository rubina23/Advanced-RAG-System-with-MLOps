# 📄 DocuMind: Intelligent Document Assistant

DocuMind is an AI-powered document intelligence platform designed to analyze, summarize, and query complex documents instantly. Whether you are dealing with clinical reports, research papers, or technical documentation, DocuMind provides precise, evidence-based insights through a conversational interface.

### 🌐 Live Access
* **Frontend (User Interface):** https://advanced-rag-system-with-mlops.streamlit.app/ 
* **Backend API (Swagger UI):** https://advanced-rag-system-with-mlops.onrender.com/docs 

---

## ✨ Key Features
* **Modern RAG Architecture:** Built using LangChain (LCEL), FastAPI, and Google Gemini for high-performance and scalability.
* **Smart Analysis:** Upload research papers or clinical reports to get instant summaries and clear answers.
* **High-Performance Vector DB:** Utilizes **FAISS** for lightning-fast semantic similarity search and context retrieval.
* **Context-Aware Q&A:** Get precise, evidence-based responses grounded in your uploaded documents.
* **RESTful API:** decoupled client-server architecture with a fully documented backend using **FastAPI**.
* **Healthcare Ready:** Specialized in extracting critical patient data, symptoms, and medical findings from clinical notes.

---

## 🛠️ Tech Stack
* **LLM Engine:** Google Gemini AI
* **Framework:** LangChain (LCEL)
* **Backend:** Python, FastAPI, Uvicorn
* **Frontend:** Streamlit, Requests
* **Vector Database:** FAISS (Facebook AI Similarity Search)
* **Deployment:** Render (Backend), Streamlit Community Cloud (Frontend)
  
---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/rubina23/Advanced-RAG-System-with-MLOps 
cd Advanced-RAG-System-with-MLOps

```
### 2. Create a Virtual Environment & Install Dependencies
```
python -m venv venv
source venv/Scripts/activate  # For Windows
pip install -r requirements.txt

```
### 3. Setup Environment Variables
Create a .env file in the root directory and add your Gemini API key:
```
GEMINI_API_KEY=your_google_gemini_api_key_here

```
### 4. Run the Backend (FastAPI)
```
uvicorn main:app --reload
```
The API will be available at http://localhost:8000/docs

### 5. Run the Frontend (Streamlit)
Open a new terminal, activate the environment, and run:
```
streamlit run frontend.py

```
The Chat UI will open in your default browser.


## 🏗️ Project Architecture
DocuMind utilizes a Retrieval-Augmented Generation (RAG) pipeline:
- Ingestion: PDF parsing via PyPDFLoader.
- Processing: Recursive text splitting for optimized context retrieval.
- Vectorization: FAISS indexing for fast semantic search.
- Generation: LCEL-based chain using Google Gemini for accurate, context-aware responses.
  
Developed as part of an AI engineering journey focusing on Healthcare Informatics and GenAI solutions.
