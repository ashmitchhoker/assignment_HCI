# Quick Reference - RAG Chatbot Integration

## Setup Commands

```bash
# 1. Install Python dependencies
cd backend
python -m venv venv
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt

# 2. Test RAG service
npm run test:rag

# 3. Start backend
npm run dev

# 4. Start frontend (separate terminal)
cd ../frontend
npm run dev
```

## Required Environment Variables

Add these to `backend/.env`:

```env
RAG_PROVIDER=google
GOOGLE_API_KEY=your_google_api_key
HUGGINGFACEHUB_API_TOKEN=your_hf_token
HF_TOKEN=your_hf_token
HUGGINGFACE_TOKEN=your_hf_token
```

## Getting API Keys

- **Google Gemini**: https://makersuite.google.com/app/apikey
- **HuggingFace**: https://huggingface.co/settings/tokens
- **Groq** (optional): https://console.groq.com/

