import streamlit as st

from quiz.diagram_utils import create_score_pie_chart


def render_results():

    st.title("🏆 Quiz Results")

    result = st.session_state.get("last_result")

    if not result:
        st.info(
            "No quiz results yet. Take a quiz first."
        )
        return

    st.markdown(
        f"### Score: {result['score']} / "
        f"{result['total']} "
        f"({result['percentage']}%)"
    )

    fig = create_score_pie_chart(
        result["score"],
        result["total"] - result["score"]
    )

    st.pyplot(fig)

    st.markdown("### Review")

    for i, item in enumerate(
        result["review"],
        1
    ):

        icon = "✅" if item["is_correct"] else "❌"

        st.write(
            f"{icon} **Q{i}: {item['question']}**"
        )

        st.write(
            f"Your answer: {item['your_answer']}"
        )

        st.write(
            f"Correct answer: {item['correct_answer']}"
        )

        st.markdown("---")