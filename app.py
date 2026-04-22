import streamlit as st
from utils import (
    extract_text_from_pdf,
    extract_details,
    clean_text,
    calculate_similarity,
    overall_score
)

st.set_page_config(page_title="SmartHire AI", layout="wide")

st.title("SmartHire AI - Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file:
    with open("resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    text = extract_text_from_pdf("resume.pdf")

    details = extract_details(text)

    clean = clean_text(text)

    scores = calculate_similarity(clean)
    overall = overall_score(scores)

    st.subheader("Candidate Details")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Name:** {details['Name']}")
        st.write(f"**Email:** {details['Email']}")
        st.write(f"**Phone:** {details['Phone']}")

    with col2:
        st.write(f"**Gender:** {details['Gender']}")
        st.write(f"**Education:** {details['Education']}")
        st.write(f"**Experience:** {details['Experience']}")

    st.subheader(f"Overall Match: {overall}%")

    best_domain = max(scores, key=scores.get)
    st.success(f"Best Suitable Role: {best_domain}")

    st.write("###  Domain-wise Scores")
    for domain, score in scores.items():
        st.write(f"{domain}: {score}%")

    st.write("### Visualization")
    st.bar_chart(scores)

    st.write("### Improvement Suggestions")

    for domain, score in scores.items():
        if score < 40:
            st.warning(f"Improve skills in {domain}")