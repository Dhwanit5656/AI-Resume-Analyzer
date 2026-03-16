import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from prompt import prompt1
from dotenv import load_dotenv
import tempfile

load_dotenv()

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Analyze how well your resume matches a job description using AI.")

# Sidebar
st.sidebar.title("Upload Resume")

uploaded_file = st.sidebar.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "This AI tool compares your resume with a job description and provides an ATS match score."
)

# Main layout
job_desc = st.text_area(
    "Paste Job Description",
    height=200
)

analyze_button = st.button("🚀 Analyze Resume")

if analyze_button:

    if uploaded_file is None:
        st.warning("Please upload a resume.")
    
    elif job_desc.strip() == "":
        st.warning("Please enter a job description.")

    else:

        with st.spinner("Analyzing resume with AI..."):

            # Save uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(uploaded_file.read())
                filepath = tmp_file.name

            loader = PyPDFLoader(filepath)
            docs = loader.load()

            resume_text = "\n".join([doc.page_content for doc in docs])

            prompt = PromptTemplate(
                template=prompt1,
                input_variables=["job_description", "resume_text"]
            )

            llm = HuggingFaceEndpoint(
                repo_id="meta-llama/Llama-3.1-8B-Instruct",
                task="text-generation",
                max_new_tokens=2048
            )

            model = ChatHuggingFace(llm=llm)

            parser = StrOutputParser()

            chain = prompt | model | parser

            response = chain.invoke({
                "job_description": job_desc,
                "resume_text": resume_text
            })

        st.success("Analysis Complete ✅")

        st.markdown("## 📊 Resume Analysis Result")

        st.markdown(response)