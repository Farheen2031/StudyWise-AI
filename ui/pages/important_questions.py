import streamlit as st
from database.db_handler import get_all_materials, get_material_by_id
from ai_features.question_recommender import generate_important_questions
from ai_features.qa_engine import answer_question


def render_important_questions():
    st.title("❓ Important Questions & Answers")

    materials = get_all_materials()

    if not materials:
        st.info("Upload material first.")
        return

    options = {
        f"{m['filename']} ({m['subject']})": m["id"]
        for m in materials
    }

    choice = st.selectbox("Choose material", list(options.keys()))
    material = get_material_by_id(options[choice])

    if st.button("Generate Important Questions"):
        with st.spinner("Analyzing material..."):
            questions = generate_important_questions(
                material["extracted_text"],
                num_questions=6
            )

        st.markdown("### Likely Important Questions")

        for i, q in enumerate(questions, 1):
            st.write(f"{i}. {q}")

    st.markdown("---")
    st.subheader("Ask Your Own Question")

    user_question = st.text_input(
        "Type a question about this material"
    )

    if st.button("Get Answer") and user_question:
        with st.spinner("Searching material..."):
            answer = answer_question(
                material["extracted_text"],
                user_question
            )

        st.markdown("### Answer")
        st.write(answer)
