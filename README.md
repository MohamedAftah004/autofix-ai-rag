# 🚗 AutoFix AI

Guarded RAG System for Automotive Diagnostics

AutoFix AI is a lightweight Agentic AI system that helps diagnose car issues based strictly on a predefined knowledge base.

The system retrieves relevant fault data, generates a response using an LLM, and applies guardrails to prevent hallucination or unsupported assumptions.

---

## 🎯 Problem

Car owners often describe issues in natural language.  
Traditional keyword matching fails.  
LLMs may hallucinate unsupported solutions.

AutoFix AI solves this by combining:

- Controlled Retrieval (TF-IDF + Cosine Similarity)
- Strict Prompt Guardrails
- Output Validation Layer

---

## 🧠 System Architecture

User Input  
→ Input Analyzer  
→ Fault Retriever  
→ Diagnosis Agent (LLM)  
→ Critic & Validator  
→ Final Response

---

## 🛡️ Hallucination Protection

The system prevents unsupported answers by:

- Enforcing strict prompt rules
- Blocking speculative language
- Applying confidence thresholds
- Returning explicit "data not available" responses when needed

---

## ⚙️ Tech Stack

- Python
- FastAPI
- TF-IDF Vectorization
- Cosine Similarity
- OpenAI-compatible LLM API
- Pydantic
- Pandas

---

## 📂 Project Structure

app/
│
├── agents/
│ ├── analyzer.py
│ ├── retriever.py
│ ├── diagnosis_agent.py
│ ├── critic_agent.py
│ └── validator.py
│
├── data/
│ └── faults.csv
│
├── llm/
│ └── client.py
│
├── schemas.py
├── config.py
└── main.py

---

## 🚀 Running the Project

1. Install dependencies:
   pip install -r requirements.txt

2. Run the API:
   uvicorn app.main:app --reload

3. Send a request:

POST `/diagnose`

```json
{
  "description": "العربية بتسخن بسرعة وبتطفي",
  "car_model": "Hyundai Elantra"
}
```

Response Example
{
"diagnosis": "...",
"confidence": 0.73
}
