import os
import tempfile
from fastapi import FastAPI, UploadFile, File, Form
from dotenv import load_dotenv

# নতুন এবং আপডেটেড ইমপোর্টস (langchain.chains বাদ দেওয়া হয়েছে)
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

app = FastAPI(title="AI Document Assistant API", description="Smart Document Chatbot (Modern LCEL Architecture)")

# গ্লোবাল ভেরিয়েবল
vector_store = None

# AI মডেল সেটআপ
#  embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
# llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
# llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")
# llm = ChatGoogleGenerativeAI(model="gemini-pro")
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

@app.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    global vector_store
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(await file.read())
        tmp_path = tmp_file.name

    try:
        loader = PyPDFLoader(tmp_path)
        documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_documents(documents)

        vector_store = FAISS.from_documents(chunks, embeddings)
        
        return {"status": "success", "message": f"'{file.filename}' সফলভাবে প্রসেস করা হয়েছে!"}
    
    finally:
        os.remove(tmp_path)

# ডেটা সাজানোর জন্য ছোট্ট হেল্পার ফাংশন
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

@app.post("/ask/")
async def ask_question(question: str = Form(...)):
    global vector_store
    
    if vector_store is None:
        return {"error": "দয়া করে প্রথমে একটি ডকুমেন্ট আপলোড করুন।"}

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    system_prompt = (
        "You are a highly intelligent AI assistant. "
        "Use the following pieces of retrieved context to answer the question. "
        "If you don't know the answer, just say that you don't know. "
        "Keep the answer concise and accurate in the language the user asked."
        "\n\n"
        "{context}"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

    # আধুনিক LCEL (LangChain Expression Language) পাইপলাইন
    rag_chain = (
        {"context": retriever | format_docs, "input": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    # উত্তর জেনারেট করা
    answer = rag_chain.invoke(question)

    return {
        "question": question, 
        "answer": answer
    }


@app.get("/")
async def root():
    return {"message": "স্বাগতম! AI Document Assistant সার্ভার সফলভাবে চলছে। দয়া করে /docs লিংকে গিয়ে API টেস্ট করুন।"}