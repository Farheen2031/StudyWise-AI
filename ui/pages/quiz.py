import streamlit as st
from database.db_handler import (
    get_all_materials,
    get_material_by_id,
    save_quiz_result
)
from quiz.mcq_generator import generate_mcqs
from quiz.quiz_engine import calculate_score


def render_quiz():
    st.title("🧠 Quiz")

    materials = get_all_materials()

    if not materials:
        st.info("Upload material first.")
        return

    options = {
        f"{m['filename']} ({m['subject']})": m["id"]
        for m in materials
    }

    choice = st.selectbox("Choose material", list(options.keys()))
    num_questions = st.slider("Number of questions", 3, 10, 5)

    if st.button("Start Quiz"):
        material = get_material_by_id(options[choice])

        with st.spinner("Generating quiz..."):
            mcqs = generate_mcqs(
                material["extracted_text"],
                num_questions
            )

        if not mcqs:
            st.error("Couldn't generate questions from this material.")
            return

        st.session_state.quiz_mcqs = mcqs
        st.session_state.quiz_material_id = material["id"]
        st.session_state.quiz_subject = material["subject"]
        st.session_state.quiz_started = True

    if st.session_state.get("quiz_started", False):
        mcqs = st.session_state.quiz_mcqs

        st.markdown("---")
        st.subheader("Answer the Questions")

        user_answers = []

        for i, mcq in enumerate(mcqs, 1):
            st.write(f"**{i}. {mcq['question']}**")

            answer = st.radio(
                "Choose an answer:",
                mcq["options"],
                key=f"quiz_answer_{i}"
            )

            user_answers.append(answer)

        if st.button("Submit Quiz"):
            result = calculate_score(mcqs, user_answers)

            save_quiz_result(
                st.session_state.quiz_material_id,
                st.session_state.quiz_subject,
                result["score"],
                result["total"],
                result["percentage"]
            )

            st.session_state.quiz_result = result
            st.session_state.quiz_started = False

    if "quiz_result" in st.session_state:
        result = st.session_state.quiz_result

        st.markdown("---")
        st.subheader("Quiz Result")

        st.success(
            f"Score: {result['score']}/{result['total']} "
            f"({result['percentage']}%)"
        )

        st.subheader("Answer Review")

        for i, review in enumerate(result["review"], 1):
            st.write(f"**{i}. {review['question']}**")
            st.write(f"Your answer: {review['your_answer']}")
            st.write(f"Correct answer: {review['correct_answer']}")

            if review["is_correct"]:
                st.success("Correct")
            else:
                st.error("Incorrect")
