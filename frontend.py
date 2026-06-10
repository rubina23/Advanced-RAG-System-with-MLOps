import streamlit as st
import requests

# Render-live API link
API_URL = "https://advanced-rag-system-with-mlops.onrender.com"

# Setup page title & layout
st.set_page_config(page_title="DocuMind AI", page_icon="📄", layout="centered")
st.title("📄 Advanced RAG Document Assistant")
st.markdown("Upload a research paper or document and ask anything!")

# Docs Upload section
with st.sidebar:
    st.header("📂 Upload Document")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    
    if st.button("Process Document"):
        if uploaded_file is not None:
            with st.spinner("Processing document... Please wait."):
                # preparing file to sent API 
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
                response = requests.post(f"{API_URL}/upload/", files=files)
                
                if response.status_code == 200:
                    st.success("Document successfully processed!")
                else:
                    st.error("Error processing document. Please try again.")
        else:
            st.warning("Please upload a PDF file first.")

# create session state for save chat history 
if "messages" not in st.session_state:
    st.session_state.messages = []

# Shown previous messages on the screen 
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# chatbox for user input 
if prompt := st.chat_input("Ask a question about your document..."):
    # shown message of user on the screen  
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Answer of AI from API
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                payload = {"question": prompt}
                response = requests.post(f"{API_URL}/ask", data=payload)
                
                if response.status_code == 200:
                    answer = response.json().get("answer", "Sorry, I couldn't find an answer.")
                    st.markdown(answer)
                    # Save AI answer on the history 
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                else:
                    st.error(f"Server Error {response.status_code}: {response.text}")

            #     if response.status_code == 200:
            #         answer = response.json().get("answer", "Sorry, I couldn't find an answer.")
            #         st.markdown(answer)
            #         # AI answer Save on the history  
            #         st.session_state.messages.append({"role": "assistant", "content": answer})
            #     else:
            #         st.error("Failed to get response. Please ensure a document is uploaded.")
            except Exception as e:
                st.error(f"Server is not responding: {e}")