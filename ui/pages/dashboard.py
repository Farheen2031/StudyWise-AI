import streamlit as st
from database.db_handler import get_all_materials, get_quiz_history
from ui.components import render_metric_card, render_item, render_page_header

def render_dashboard():
    materials=get_all_materials(); quizzes=get_quiz_history()
    subjects=set(m["subject"] for m in materials)
    render_page_header("Dashboard","A quick view of your study activity and recent progress.")
    c1,c2,c3=st.columns(3)
    with c1: render_metric_card(len(materials),"Materials uploaded","📚")
    with c2: render_metric_card(len(subjects),"Subjects covered","🗂️")
    with c3: render_metric_card(len(quizzes),"Quizzes taken","🧠")
    st.markdown('<div class="sw-section"><div><h2>Recent materials</h2><p>Your latest uploaded study resources.</p></div></div>',unsafe_allow_html=True)
    if materials:
        for m in materials[:5]: render_item(m["filename"],f'{m["subject"]} · {m["page_count"]} pages · {m["upload_date"]}',"📄")
    else: st.markdown('<div class="sw-empty">📚 No materials uploaded yet.<br>Upload your first PDF to start building your study workspace.</div>',unsafe_allow_html=True)
    st.markdown('<div class="sw-section"><div><h2>Recent quiz scores</h2><p>Your latest practice results.</p></div></div>',unsafe_allow_html=True)
    if quizzes:
        for q in quizzes[:5]: render_item(q["subject"],f'Score {q["score"]}/{q["total"]} · {q["percentage"]}% · {q.get("taken_date","")}',"🏆")
    else: st.markdown('<div class="sw-empty">🧠 No quizzes taken yet. Try a quiz after uploading study material.</div>',unsafe_allow_html=True)
