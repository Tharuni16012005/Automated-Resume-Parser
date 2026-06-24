import pdfplumber
import re

SKILLS = [
    "Python", "Java", "C", "C++", "Machine Learning",
    "Data Science", "Flask", "SQL", "HTML", "CSS",
    "JavaScript", "TensorFlow", "Pandas", "NumPy",
    "OpenCV", "Git", "GitHub", "AWS"
]

def extract_resume_data(filepath):

    text = ""

    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

    email = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    phone = re.findall(
        r"\+?\d[\d\s-]{8,}\d",
        text
    )

    name = text.split("\n")[0] if text else "Not Found"

    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    education_keywords = [
        "B.Tech",
        "Bachelor of Technology",
        "B.E",
        "Bachelor of Engineering",
        "M.Tech",
        "Diploma",
        "Intermediate",
        "SSC"
    ]

    found_education = []

    for edu in education_keywords:
        if edu.lower() in text.lower():
            found_education.append(edu)

    return {
        "name": name,
        "email": email[0] if email else "Not Found",
        "phone": phone[0] if phone else "Not Found",
        "skills": ", ".join(found_skills) if found_skills else "Not Found",
        "education": ", ".join(found_education) if found_education else "Not Found"
    }