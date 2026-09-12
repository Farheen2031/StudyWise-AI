import streamlit as st

from database.db_handler import init_db
from quiz.mcq_generator import generate_mcqs

st.set_page_config(
    page_title="StudyWise AI",
    page_icon="📚",
    layout="wide"
)

init_db()

st.title("📚 StudyWise AI")
st.write("AI-Based Study Material Organizer and Question Generator")

st.success("StudyWise AI is running successfully!")

st.header("📄 Study Material")

text = st.text_area(
    "Paste your study material here:",
    height=200
)

if st.button("Generate Quiz"):
    if not text.strip():
        st.warning("Please enter study material first.")
    else:
        quiz = generate_mcqs(text)

        st.subheader("📄 Generated Quiz")

        if not quiz:
            st.info("No quiz questions could be generated from this material.")
        else:
            for i, question in enumerate(quiz, 1):
                st.write(f"**{i}. {question['question']}**")
                for option in question["options"]:
                    st.write(f"- {option}")