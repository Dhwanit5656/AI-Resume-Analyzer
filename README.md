# 📄 AI Resume Analyzer

An intelligent resume analysis tool that compares your resume against a job description, gives an ATS match score, and provides actionable improvement suggestions — powered by LangChain, HuggingFace, and Streamlit.

---

## ✨ Features

- 📤 **PDF Resume Upload** — Easily upload your resume directly in the sidebar
- 🤖 **AI-Powered Analysis** — Uses Llama 3.1 8B to deeply evaluate your resume vs. job description
- 📊 **ATS Match Score** — Get a 0–100% compatibility score instantly
- 🔍 **Skill Gap Analysis** — See exactly which skills you're missing for the role
- 💡 **Improvement Suggestions** — Actionable tips to strengthen your resume
- 🏷️ **ATS Optimization Tips** — Keyword and formatting advice to pass applicant tracking systems
- 🖥️ **Clean Wide-Layout UI** — Intuitive Streamlit interface with sidebar upload

---

## 📋 Analysis Breakdown

For every resume + job description pair, the tool returns:

| Section | Description |
|---|---|
| **Overall Match Score** | Percentage match between resume and job |
| **Key Skills Matched** | Skills from your resume that align with the role |
| **Missing Skills** | Required skills not found in your resume |
| **Strengths** | Strong projects, tech, or experience highlights |
| **Weaknesses / Gaps** | Areas that need improvement |
| **Improvement Suggestions** | Clear, specific resume edits to increase fit |
| **ATS Optimization Tips** | Keywords and formatting fixes for ATS compatibility |

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Frontend | [Streamlit](https://streamlit.io/) |
| LLM | `meta-llama/Llama-3.1-8B-Instruct` via HuggingFace |
| RAG Framework | LangChain |
| PDF Loader | `PyPDFLoader` (LangChain Community) |
| Prompt Engine | `PromptTemplate` (LangChain Core) |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the root directory:

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
```

> Get your free API token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

### 4. Run the app

```bash
streamlit run app.py
```

---

## 📦 Requirements

```
streamlit
langchain
langchain-huggingface
langchain-community
python-dotenv
pypdf
```

---

## 🖼️ Usage

1. **Upload your resume** (PDF) using the sidebar uploader
2. **Paste the job description** into the text area on the main page
3. Click **"🚀 Analyze Resume"**
4. Review the detailed AI analysis output

---

## 📁 Project Structure

```
ai-resume-analyzer/
│
├── app.py              # Main Streamlit application
├── prompt.py           # LLM prompt template
├── .env                # API keys (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Configuration

You can adjust the following in `app.py`:

| Parameter | Default | Description |
|---|---|---|
| `max_new_tokens` | `2048` | Maximum length of AI response |
| `repo_id` | `meta-llama/Llama-3.1-8B-Instruct` | HuggingFace model to use |
| `height` | `200` | Height of the job description text area |

---

## 📝 Notes

- Only **PDF** resumes are supported at this time
- The LLM is loaded fresh on each analysis — no session state is maintained
- For best results, paste the **full job description** including requirements and responsibilities

---

## 🙌 Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain) for the LLM pipeline
- [HuggingFace](https://huggingface.co/) for model hosting
- [Streamlit](https://streamlit.io/) for the UI framework
- [Meta AI](https://ai.meta.com/) for the Llama 3.1 model
