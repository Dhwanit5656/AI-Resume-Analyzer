# AI Resume Analyzer 📄✨

An AI-powered tool that helps you understand how well your resume matches a specific job description.

It extracts text from your PDF resume, compares it with the pasted job description, and uses a language model to generate:

- match percentage estimation
- strong matching areas
- missing keywords/skills
- ATS-friendliness feedback
- improvement suggestions

Built with Streamlit + LangChain + Hugging Face Inference (Llama 3.1 8B Instruct)

## Screenshots

*(Add 1–3 screenshots here later – e.g. upload + analysis result)*

<!-- You can later replace this with real images like: -->
<!-- ![Upload screen](screenshots/upload.png) -->
<!-- ![Result example](screenshots/result.png) -->

## Features

- Upload resume (PDF only)
- Paste job description
- AI-powered semantic matching & keyword analysis
- Clean, readable markdown output
- Uses Meta's Llama-3.1-8B-Instruct via Hugging Face

## Tech Stack

- **Frontend**: Streamlit
- **LLM**: meta-llama/Llama-3.1-8B-Instruct (Hugging Face Inference)
- **PDF parsing**: PyPDFLoader (LangChain)
- **Orchestration**: LangChain (PromptTemplate + ChatHuggingFace)
- **Environment**: python-dotenv

## Quick Start (Local)

### 1. Clone & install

```bash
git clone https://github.com/YOUR-USERNAME/ai-resume-analyzer.git
cd ai-resume-analyzer

# Recommended: virtual environment
python -m venv venv
source venv/bin/activate     # Linux/macOS
# or
venv\Scripts\activate        # Windows

pip install -r requirements.txt
```
###2. Get your Hugging Face Access Token & create .env file
1.Go to: https://huggingface.co/settings/tokens
2.Click New token → give it a name (e.g. "resume-analyzer") → select Read role → Create
3.Copy the token (starts with hf_)
4.Important: You also need to be approved for the model:
  - Visit https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct
  - Accept the license / request access (usually instant or within hours)
5.In the project root folder, create a file named exactly .env and paste:
  HUGGINGFACEHUB_API_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

###3. Run the app
streamlit run app.py
Open http://localhost:8501 in your browser
Upload a PDF resume, paste a job description, and click "Analyze Resume"

You should see the analysis result in a few seconds (depending on Hugging Face server load).
