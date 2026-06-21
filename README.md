# 🤖 FAQ Chatbot using NLP (CodeAlpha Internship Project)

This is a simple FAQ Chatbot built using Python, Flask, and NLP techniques. It uses TF-IDF Vectorization and Cosine Similarity to match user questions with the most relevant FAQ answer.

## 🚀 Features
- NLP-based question understanding
- TF-IDF vectorization
- Cosine similarity matching
- Flask backend API
- Interactive chat UI
- Easy-to-edit FAQ dataset

## 🛠️ Tech Stack
- Python 🐍
- Flask 🌐
- Scikit-learn 🤖
- HTML, CSS, JavaScript 💻

## 📁 Project Structure
faq_chatbot/
│
├── app.py
├── chatbot.py
├── faq_data.py
├── requirements.txt
└── templates/
    └── index.html

## ⚙️ Installation & Setup

### 1. Clone repository
git clone https://github.com/naddimounika09/faq-chatbot.git
cd faq-chatbot

### 2. Create virtual environment (optional)
python -m venv .venv
.venv\Scripts\activate   (Windows)

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run project
python app.py

### 5. Open in browser
http://127.0.0.1:5000

## 💡 How It Works
User enters question → Text cleaned → TF-IDF converts text → Cosine similarity finds best match → Bot returns answer

## 📊 Example Questions
- What is your return policy?
- How can I track my order?
- Do you offer free shipping?
- How can I contact support?

## 🎯 Future Improvements
- Add AI semantic search (Sentence-BERT)
- Add voice input/output
- Improve UI with animations
- Deploy online (Render/PythonAnywhere)

## 👩‍💻 Author
Mounika – CodeAlpha Internship Project 🚀
