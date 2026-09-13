"""
app.py
Main entry point for StudyWise AI. Wires together all team members' modules.
"""

import streamlit as st
from database.db_handler import init_db, init_quiz_table
from ui.styles import apply_custom_css
from ui.components import render_sidebar_nav
from ui.pages.home import render_home
from ui.pages.dashboard import render_dashboard
from ui.pages.upload import render_upload
from ui.pages.materials import render_materials
from ui.pages.summary import render_summary
from ui.pages.important_questions import render_important_questions
from ui.pages.quiz import render_quiz
from ui.pages.results import render_results

st.set_page_config(page_title="StudyWise AI", page_icon="📖", layout="wide")

init_db()
init_quiz_table()
apply_custom_css()

page = render_sidebar_nav()

if page == "home":
    render_home()
elif page == "dashboard":
    render_dashboard()
elif page == "upload":
    render_upload()
elif page == "materials":
    render_materials()
elif page == "summary":
    render_summary()
elif page == "important_questions":
    render_important_questions()
elif page == "quiz":
    render_quiz()
elif page == "results":
    render_results()