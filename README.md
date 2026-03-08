# 🌾 Yojana Mitra — योजना मित्र — యోజన మిత్ర

> **Your guide to every government agriculture scheme in Telangana.**  
> Ask in English, Telugu, or Hindi. Get plain-language answers instantly.

---

## The Problem

India has dozens of central and state welfare schemes for farmers — Rythu Bandhu, PM-KISAN, PMFBY crop insurance, Kisan Credit Card, and more. But accessing them requires:

- Visiting multiple government websites that are hard to navigate
- Running behind district agriculture offices for basic eligibility questions
- Understanding bureaucratic language in English when most farmers speak Telugu or Hindi
- Not knowing which documents to bring, or where to submit them

Most eligible farmers either never claim their benefits, or lose weeks in the process.

---

## The Solution

**Yojana Mitra** is a RAG-powered (Retrieval-Augmented Generation) chatbot that lets any farmer or citizen ask plain questions and get accurate, actionable answers — in the language they're most comfortable with.

### How it works

```
User asks a question (English / Telugu / Hindi)
        ↓
Backend detects language → translates query to English
        ↓
Semantic search across curated scheme documents (ChromaDB)
        ↓
Top relevant chunks → Gemini 1.5 Flash generates answer
        ↓
Answer returned in user's chosen language with source citations
```

---

## Features

- 🗣️ **Trilingual** — English, Telugu (తెలుగు), Hindi (हिन्दी) — UI and chat answers
- 📋 **Scheme-aware answers** — eligibility, required documents, how to apply, helplines
- 💬 **Suggested prompts** — tap-to-ask questions so farmers know where to start
- 👤 **One-time onboarding** — saves name, district, land size to personalise answers
- 📱 **Mobile-first** — designed for smartphone use, works on any screen size
- 🔒 **Rate limited** — prevents abuse of free-tier APIs
- 📄 **Source cited** — every answer shows which document it came from

---

## Schemes Covered

| Scheme | Type | Benefit |
|--------|------|---------|
| Rythu Bandhu | Telangana | ₹10,000/acre/year investment support |
| Rythu Bima | Telangana | ₹5 lakh life insurance for farmers |
| PM-KISAN | Central | ₹6,000/year direct benefit transfer |
| PMFBY | Central | Crop insurance against natural disasters |
| Kisan Credit Card | Central | Short-term credit at 4% interest |
| Soil Health Card | Central | Free soil testing and crop recommendations |
| PM Kisan Maan Dhan | Central | ₹3,000/month pension after age 60 |
| e-NAM | Central | Digital marketplace for agricultural produce |
| Telangana TMIP | Telangana | Micro irrigation project subsidies |

---

## Tech Stack

| Layer | Technology | Why |
|-------|-----------|-----|
| Frontend | React + Vite | Fast SPA, mobile-first |
| Styling | Tailwind CSS | Responsive design with minimal code |
| Routing | React Router | Landing page → Chat navigation |
| i18n | react-i18next | EN / Telugu / Hindi language switching |
| Backend | FastAPI (Python) | Async, fast, great for AI workloads |
| LLM | Google Gemini 1.5 Flash | Free tier, native multilingual support |
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) | Free, local, high quality |
| Vector DB | ChromaDB (local) / Pinecone (prod) | Semantic scheme retrieval |
| Orchestration | LangChain | RAG chain and document processing |
| Translation | deep-translator + langdetect | Telugu/Hindi query → English for retrieval |
| Fonts | Noto Sans (Google Fonts) | Correct rendering of Telugu and Devanagari scripts |
| Frontend Deploy | Vercel (free) | Zero-config, auto-deploys on push |
| Backend Deploy | Render (free tier) | FastAPI hosting |
| CI/CD | GitHub Actions | Auto-deploy on push to main |

---

## Project Structure

```
yojana-mitra/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app, CORS, rate limiting
│   │   ├── rag/
│   │   │   ├── ingest.py        # PDF/TXT → vector DB pipeline
│   │   │   ├── retriever.py     # ChromaDB semantic search
│   │   │   └── chain.py         # Gemini RAG chain
│   │   ├── routers/
│   │   │   └── chat.py          # POST /api/v1/chat
│   │   └── utils/
│   │       └── translate.py     # Language detection + translation
│   ├── data/
│   │   ├── raw/                 # Downloaded scheme PDFs
│   │   └── summaries/           # Hand-curated scheme summaries (.txt)
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── i18n/
│   │   │   └── locales/         # en.json, te.json, hi.json
│   │   ├── components/
│   │   │   ├── LanguageSwitcher.jsx
│   │   │   ├── OnboardingModal.jsx
│   │   │   └── SuggestedPrompts.jsx
│   │   └── pages/
│   │       ├── Landing.jsx      # Landing page
│   │       └── Chat.jsx         # Chat interface
│   └── package.json
└── .github/workflows/           # CI/CD pipelines
```

---

## Getting Started (Local)

### Prerequisites
- macOS with Homebrew
- Python 3.11
- Node.js (for running Vite + React only — no backend Node usage)
- Gemini API key — free at [aistudio.google.com](https://aistudio.google.com)

### Setup steps

1. Clone the repo
2. Set up Python virtual environment in `backend/`, install dependencies from `requirements.txt`
3. Create `backend/.env` with your Gemini and Pinecone API keys
4. Add scheme documents to `backend/data/` and run the ingestion pipeline
5. Start the FastAPI backend on port 8000
6. Install frontend dependencies and start the React dev server on port 5173

Full step-by-step instructions are in the implementation guide.

---

## Deployment

- **Frontend:** Vercel — connect repo, set root to `frontend`, add `VITE_API_BASE_URL` env var
- **Backend:** Render — connect repo, set root to `backend`, add API keys as env vars
- **Auto-deploy:** GitHub Actions triggers on every push to `main`

---

## Data Sources

- [Telangana Agriculture Department](https://agri.telangana.gov.in)
- [Rythu Bandhu Portal](https://rythubandhu.telangana.gov.in)
- [PM-KISAN](https://pmkisan.gov.in)
- [PMFBY Crop Insurance](https://pmfby.gov.in)
- [NABARD (Kisan Credit Card)](https://nabard.org)
- [Soil Health Card Scheme](https://soilhealth.dac.gov.in)

---

## Disclaimer

Yojana Mitra is an informational tool built to simplify access to public scheme information. Always verify eligibility and application details at the official government portals or your local agriculture office.

---

*Built to make every government scheme accessible to every farmer.* 🌾
