import streamlit as st
from database.db_handler import get_all_materials, get_material_by_id
from ai_features.question_recommender import generate_important_questions
from ai_features.qa_engine import answer_question
from ui.components import render_page_header

def render_important_questions():
    render_page_header("Important questions","Find likely exam questions and ask your own questions about a material.")
    materials=get_all_materials()
    if not materials: st.info("Upload material first."); return
    options={f'{m["filename"]} · {m["subject"]}':m["id"] for m in materials}; choice=st.selectbox("Choose material",list(options.keys())); material=get_material_by_id(options[choice])
    if st.button("Generate important questions",type="primary"):
        with st.spinner("Analyzing material..."): questions=generate_important_questions(material["extracted_text"],num_questions=6)
        st.markdown('<div class="sw-panel"><h3>❓ Likely important questions</h3></div>',unsafe_allow_html=True)
        for i,q in enumerate(questions,1): st.markdown(f'<div class="sw-item"><div class="sw-item-title">{i}. {q}</div></div>',unsafe_allow_html=True)
    st.markdown('<div class="sw-section"><div><h2>Ask your own question</h2><p>Search the selected material for a relevant answer.</p></div></div>',unsafe_allow_html=True)
    user_question=st.text_input("Type a question about this material")
    if st.button("Get answer") and user_question:
        with st.spinner("Searching material..."): answer=answer_question(material["extracted_text"],user_question)
        st.markdown('<div class="sw-panel"><h3>💬 Answer</h3></div>',unsafe_allow_html=True); st.write(answer)
