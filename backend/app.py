from flask import Flask, request, jsonify
from flask_cors import CORS
import pdfplumber
import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "AI Resume Analyzer Running"


@app.route("/upload", methods=["POST"])
def upload_resume():

    # ✅ Check file
    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["resume"]

    # ✅ Extract text
    text = ""
    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # ✅ NLP
    doc = nlp(text)

    # 🎯 Skill categories
    skill_categories = {
        "Programming": ["Python", "Java", "C++"],
        "AI/ML": ["Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "Scikit-learn"],
        "Web": ["React", "Angular", "Django", "Flask", "Spring Boot"],
        "Database": ["SQL", "MongoDB", "PostgreSQL"],
        "Tools": ["Git", "Docker", "LangChain"],
        "Data": ["Pandas", "NumPy", "Data Science", "Artificial Intelligence"]
    }

    # ✅ Extract skills
    found_skills = {}
    all_found_skills = []
    text_lower = text.lower()

    for category, skills in skill_categories.items():
        found_skills[category] = []

        for skill in skills:
            if skill.lower() in text_lower:
                found_skills[category].append(skill)
                all_found_skills.append(skill)

    # Remove empty categories
    found_skills = {k: v for k, v in found_skills.items() if v}

    # ✅ Score calculation
    total_skills = sum(len(v) for v in skill_categories.values())
    matched_skills = len(set(all_found_skills))

    if total_skills > 0:
        score = int((matched_skills / total_skills) * 100)
    else:
        score = 0

    # ✅ Missing skills
    missing_skills = []
    for category, skills in skill_categories.items():
        for skill in skills:
            if skill not in all_found_skills:
                missing_skills.append(skill)

    # ✅ Improved Suggestions
    suggestions = []

    if len(missing_skills) > 0:
        suggestions.append("Add missing skills to improve your resume")

    if "React" in missing_skills:
        suggestions.append("Learn React for frontend development")

    if "Docker" in missing_skills:
        suggestions.append("Add Docker for deployment skills")

    if "MongoDB" in missing_skills:
        suggestions.append("Learn MongoDB for database knowledge")

    if "Machine Learning" not in all_found_skills:
        suggestions.append("Add Machine Learning or AI projects")

    if "Git" not in all_found_skills:
        suggestions.append("Include Git/version control experience")

    # Score-based suggestions
    if score < 60:
        suggestions.append("Your resume needs significant improvement")
    elif score < 80:
        suggestions.append("Good resume, but can be improved further")
    else:
        suggestions.append("Excellent resume")

    # ✅ Entities (optional)
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    # ✅ Final response
    return jsonify({
        "message": "Resume processed successfully",
        "preview_text": text[:400],
        "skills_by_category": found_skills,
        "all_skills": list(set(all_found_skills)),
        "missing_skills": missing_skills[:10],
        "score": score,
        "suggestions": suggestions,
        "entities": entities[:15]
    })


if __name__ == "__main__":
    app.run(debug=True)