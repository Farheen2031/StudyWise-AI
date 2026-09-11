import streamlit as st
from database.db_handler import get_all_materials, get_quiz_history
from ui.components import render_metric_card


def render_dashboard():
    st.title("📊 Dashboard")
    materials = get_all_materials()
    quizzes = get_quiz_history()

    col1, col2, col3 = st.columns(3)

    with col1:
        render_metric_card(len(materials), "Materials Uploaded")

    with col2:
        subjects = set(m["subject"] for m in materials)
        render_metric_card(len(subjects), "Subjects Covered")

    with col3:
        render_metric_card(len(quizzes), "Quizzes Taken")

    st.markdown("---")
    st.subheader("Recent Materials")

    if materials:
        for m in materials[:5]:
            st.write(
                f"📄 **{m['filename']}** — "
                f"{m['subject']} ({m['upload_date']})"
            )
    else:
        st.write("No materials uploaded yet.")

    st.subheader("Recent Quiz Scores")

    if quizzes:
        for q in quizzes[:5]:
            st.write(
                f"🧠 {q['subject']} — "
                f"{q['score']}/{q['total']} ({q['percentage']}%)"
            )
    else:
        st.write("No quizzes taken yet.")