# 📄 Advanced RAG System with MLOps

An Enterprise-Level AI Document Assistant powered by Modern LCEL Architecture (LangChain), FastAPI, and Streamlit. This system allows users to upload complex PDF documents (like research papers) and interact with them through a context-aware AI chatbot.

### 🌐 Live Links
* **Frontend (User Interface):** https://advanced-rag-system-with-mlops.streamlit.app/ 
* **Backend API (Swagger UI):** https://advanced-rag-system-with-mlops.onrender.com/docs 

---

## ✨ Key Features
* **Modern RAG Architecture:** Built using LangChain's latest Expression Language (LCEL) for robust data pipelines.
* **Smart Document Processing:** Automatically parses, chunks, and vectorizes large PDF documents.
* **High-Performance Vector DB:** Utilizes **FAISS** for lightning-fast semantic similarity search and context retrieval.
* **Interactive UI:** A ChatGPT-like conversational interface built with **Streamlit** for seamless user experience.
* **RESTful API:** decoupled client-server architecture with a fully documented backend using **FastAPI**.

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
Document Ingestion: PDF is uploaded via Streamlit and sent to the FastAPI endpoint.

- Processing: The document is split into manageable chunks using LangChain's text splitters.

- Embedding & Storage: Chunks are converted into vector embeddings and stored in FAISS memory.

- Retrieval: User queries are matched against the FAISS index to find the most relevant context.

- Generation: The context and query are passed to the LLM (Gemini) via LCEL to generate a highly accurate, grounded response.


