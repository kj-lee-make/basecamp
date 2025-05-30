# Gemini Chatbot

## Project Overview
A basic Streamlit chatbot interface using Google Gemini API (model: gemini-1.5-flash).

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run Locally
```bash
streamlit run app.py
```

## Deploy on Streamlit Cloud
1. Push to GitHub.
2. Connect repo on Streamlit Cloud.
3. Set GEMINI_API_KEY in secrets.
4. Deploy. 