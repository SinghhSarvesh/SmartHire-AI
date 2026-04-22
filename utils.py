import pdfplumber
import pytesseract
#import cv2
import nltk
from nltk.corpus import stopwords
import string
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_details(text):
    details = {}

    lines = text.split("\n")

    details["Name"] = lines[0] if lines else "Not Found"

    email = re.findall(r'\S+@\S+', text)
    details["Email"] = email[0] if email else "Not Found"

    phone = re.findall(r'\b\d{10}\b', text)
    details["Phone"] = phone[0] if phone else "Not Found"

    text_lower = text.lower()
    if "male" in text_lower:
        details["Gender"] = "Male"
    elif "female" in text_lower:
        details["Gender"] = "Female"
    else:
        details["Gender"] = "Not Found"

    if "b.tech" in text_lower or "btech" in text_lower:
        details["Education"] = "B.Tech"
    elif "m.tech" in text_lower:
        details["Education"] = "M.Tech"
    elif "mba" in text_lower:
        details["Education"] = "MBA"
    else:
        details["Education"] = "Not Found"

    exp = re.findall(r'(\d+)\s+year', text_lower)
    details["Experience"] = exp[0] + " years" if exp else "Not Found"

    return details


def clean_text(text):
    text = text.lower()
    text = ''.join([c for c in text if c not in string.punctuation])
    words = text.split()
    words = [w for w in words if w not in stopwords.words('english')]
    return " ".join(words)


domains = {
    "AI": "machine learning deep learning tensorflow pytorch nlp",
    "Data Science": "python pandas numpy data analysis visualization statistics",
    "Data Analyst": "excel sql power bi tableau data cleaning",
    "Frontend": "html css javascript react angular ui ux",
    "Backend": "node django flask api database sql",
    "Full Stack": "mern mean full stack development",
    "DevOps": "docker kubernetes aws ci cd cloud",
    "Mobile Dev": "android ios flutter react native",
    "UI/UX": "figma adobe xd wireframe prototyping design",
    "Cyber Security": "network security ethical hacking encryption",
    "Cloud": "aws azure google cloud serverless"
}


def calculate_similarity(resume_text):
    results = {}

    for domain, text in domains.items():
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([resume_text, text])
        score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
        results[domain] = round(score * 100, 2)

    return results

def overall_score(scores):
    return round(sum(scores.values()) / len(scores), 2)
