# 🚀 AI Resume Analyzer (ATS-Based Project)

An AI-powered full-stack web application that analyzes resumes, extracts skills using NLP, calculates a score, and provides improvement suggestions.

---

## 📑 Table of Contents

* Features
* Tech Stack
* How It Works
* Project Structure
* Installation
* Running the Application
* Using the Web UI
* Scoring System
* Future Improvements

---

## ✨ Features

* 📄 Upload Resume (PDF)
* 🧠 NLP-based Skill Extraction
* 📊 Resume Score Calculation
* ❌ Missing Skills Detection
* 💡 Smart Suggestions
* 🌐 Interactive React UI

---

## 🛠️ Tech Stack

### 🔹 Frontend

* React
* JavaScript
* CSS (via React components)

### 🔹 Backend

* Flask
* spaCy (Natural Language Processing)
* pdfplumber (PDF text extraction)

### 🔹 Tools & Platforms

* Git & GitHub
* Postman (API testing)
* Render (Backend deployment)

---

## ⚙️ How It Works

1. User uploads resume from React UI
2. React sends file to Flask backend
3. Backend extracts text using pdfplumber
4. spaCy processes text (NLP)
5. Skills are matched with predefined categories
6. Score is calculated
7. Suggestions are generated
8. Results are displayed in UI

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
 │   ├── public/
 │   ├── package.json
```

---

## 🛠️ Installation

### Backend

```
cd backend
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### Frontend

```
cd frontend
npm install
```

---

## ▶️ Running the Application

### Start Backend

```
python app.py
```

### Start Frontend

```
npm start
```

---

## 🌐 Using the Web UI

1. Open browser: http://localhost:3000
2. Upload resume
3. Click upload
4. View:

   * Score
   * Skills
   * Missing skills
   * Suggestions

---

## 📊 Scoring System

```
Score = (Matched Skills / Total Skills) × 100
```

👉 This is a **Resume Match Score** based on predefined skills.

---

## 🚀 Future Improvements

* Job Description Matching (Real ATS feature)
* Improved UI/UX design
* Support for DOCX files
* Advanced AI-based scoring

---

## 📌 Project Summary

> AI-powered Resume Analyzer that evaluates resumes using NLP and provides score-based insights and improvement suggestions.
