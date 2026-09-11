import streamlit as st
from ui.components import render_card


def render_home():
    st.title("📖 Welcome to StudyWise AI")
    st.markdown("### Your AI-powered study companion")

    col1, col2 = st.columns(2)

    with col1:
        render_card(
            "Upload Materials",
            "Upload PDFs across any subject — Hindi, English, Maths, Science, and more.",
            "📤"
        )

        render_card(
            "Get Summaries",
            "Instantly generate concise summaries of your study material.",
            "📝"
        )

    with col2:
        render_card(
            "Practice MCQs",
            "Auto-generated quizzes with instant scoring.",
            "🧠"
        )

        render_card(
            "Important Questions",
            "Discover the most likely exam-relevant questions.",
            "❓"
        )

    st.markdown("---")
    st.info("Use the sidebar to navigate: start by uploading your first PDF!")