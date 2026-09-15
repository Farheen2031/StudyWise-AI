"""
components.py
Reusable UI pieces: cards, metric cards, sidebar navigation, subject list.
"""

import streamlit as st

SUBJECTS = ["Hindi", "English", "Urdu", "Maths", "Science", "History", "Geography", "Computer Science", "Other"]

NAV_ITEMS = {
    "🏠 Home": "home",
    "📊 Dashboard": "dashboard",
    "📤 Upload": "upload",
    "📚 Materials": "materials",
    "📝 Summary": "summary",
    "❓ Important Questions": "important_questions",
    "🧠 Quiz": "quiz",
    "🏆 Results": "results",
}


def render_card(title, content, icon="📘"):
    st.markdown(f"""
    <div class="card">
        <h3>{icon} {title}</h3>
        <p>{content}</p>
    </div>
    """, unsafe_allow_html=True)


def render_metric_card(value, label):
    st.markdown(f"""
    <div class="metric-card">
        <h2>{value}</h2>
        <p>{label}</p>
    </div>
    """, unsafe_allow_html=True)


def render_sidebar_nav():
    st.sidebar.title("📖 StudyWise AI")
    st.sidebar.markdown("---")
    choice = st.sidebar.radio("Navigate", list(NAV_ITEMS.keys()))
    return NAV_ITEMS[choice]
