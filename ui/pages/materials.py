import streamlit as st
from database.db_handler import get_all_materials, delete_material
from ui.components import render_card, render_page_header

def render_materials():
    materials=get_all_materials(); render_page_header("Your materials","Browse and manage the study PDFs in your workspace.")
    if not materials:
        st.markdown('<div class="sw-empty">📚 No materials yet.<br>Go to Upload to add your first PDF.</div>',unsafe_allow_html=True); return
    subjects=sorted(set(m["subject"] for m in materials)); filter_subject=st.selectbox("Filter by subject",["All"]+subjects)
    shown=0
    for m in materials:
        if filter_subject!="All" and m["subject"]!=filter_subject: continue
        shown+=1; col1,col2=st.columns([5,1])
        with col1: render_card(m["filename"],f'{m["subject"]} · {m["page_count"]} pages · uploaded {m["upload_date"]}',"📄")
        with col2:
            st.write("")
            if st.button("Delete",key=f"del_{m["id"]}"): delete_material(m["id"]); st.rerun()
    if shown==0: st.info("No materials match this subject.")
