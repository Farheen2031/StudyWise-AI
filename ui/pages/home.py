import streamlit as st
from pathlib import Path

IMAGE_PATH = Path.cwd() / "assets" / "studywise.png.jpeg"


def render_home():
    col1, col2 = st.columns([1.4, 1])

    with col1:
        st.title("📖 StudyWise AI")
        st.write(
            "Your smart study workspace for organizing study materials, "
            "creating summaries, finding important questions, and practicing quizzes."
        )

    with col2:
        if IMAGE_PATH.exists():
            st.image(str(IMAGE_PATH), use_container_width=True)

    st.markdown("---")

    st.subheader("What would you like to do?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="card">
                <h3>📤 Upload Materials</h3>
                <p>Upload your PDF study materials and keep them organized by subject.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="card">
                <h3>📝 Get Summaries</h3>
                <p>Generate concise summaries from your uploaded study materials.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="card">
                <h3>🧠 Practice MCQs</h3>
                <p>Practice automatically generated multiple-choice questions.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="card">
                <h3>❓ Important Questions</h3>
                <p>Find important exam-oriented questions from your study material.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    st.info(
        "💡 Study Tip: Upload your study material first, "
        "then use summaries, important questions, and quizzes for revision."
    )