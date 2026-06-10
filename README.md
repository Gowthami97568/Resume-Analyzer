# 🚀 AI Resume Analyzer

An AI-powered web application that analyzes resumes, extracts skills, calculates a score, and provides improvement suggestions.

---

## 📌 Features

* 📄 Upload resume (PDF)
* 🧠 Extract skills using NLP (spaCy)
* 📊 Calculate resume score
* ❌ Identify missing skills
* 💡 Provide improvement suggestions
* 🧾 Show extracted entities 

---

## 🛠 Tech Stack

### Frontend

* React

### Backend

* Flask
* spaCy
* NLP
* pdfplumber

### Tools

* Postman (API testing)

---

## 📂 Project Structure

```
resume-analyzer/
 ├── backend/
 │   ├── app.py
 │   ├── requirements.txt
 │
 ├── frontend/
 │   ├── src/
 │   ├── package.json
```

---

## ⚙️ Setup Instructions

### 🔹 Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python app.py
```

---

### 🔹 Frontend Setup

```bash
cd frontend
npm install
npm start
```

---

## 🌐 Usage

1. Open the React app in browser
2. Upload your resume (PDF)
3. View:

   * Score 📊
   * Skills ✅
   * Missing skills ❌
   * Suggestions 💡

---

## 🚀 Deployment

* Frontend → Vercel
* Backend → Render

---

## 📸 Screenshots

(Add your project screenshots here)

---

## 💡 Future Improvements

* Better UI design
* Add authentication
* Support DOCX files
* Advanced AI scoring

---

## ⭐ Acknowledgment

This project uses open-source libraries like Flask, React, and spaCy.
