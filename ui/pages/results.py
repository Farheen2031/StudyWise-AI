import streamlit as st

from quiz.diagram_utils import create_score_pie_chart
from database.db_handler import get_quiz_history


def render_results():

    st.title("🏆 Quiz Results")

    result = st.session_state.get("last_result")

    if result:
        st.markdown(
            f"### Latest Score: {result['score']} / "
            f"{result['total']} "
            f"({result['percentage']}%)"
        )

        fig = create_score_pie_chart(
            result["score"],
            result["total"] - result["score"]
        )

        st.pyplot(fig)

        st.markdown("### Review")

        for i, item in enumerate(result["review"], 1):
            icon = "✅" if item["is_correct"] else "❌"

            st.write(f"{icon} **Q{i}: {item['question']}**")
            st.write(f"Your answer: {item['your_answer']}")
            st.write(f"Correct answer: {item['correct_answer']}")
            st.markdown("---")

    st.markdown("## Quiz History")

    try:
        history = get_quiz_history()
    except Exception as e:
        st.error("Could not load quiz history from the database.")
        st.caption(f"Details: {e}")
        return

    if not history:
        st.info("No saved quiz attempts yet. Take a quiz to see your history here.")
        return

    rows = []
    for item in history:
        rows.append({
            "Subject": item.get("subject") or "Unknown",
            "Score": f"{item.get('score', 0)}/{item.get('total', 0)}",
            "Percentage": f"{round(item.get('percentage') or 0, 1)}%",
            "Date": item.get("taken_date") or "-",
        })

    st.dataframe(rows, use_container_width=True)