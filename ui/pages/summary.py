import streamlit as st
from database.db_handler import get_all_materials, get_material_by_id
from ai_features.summary_generator import generate_summary
from ui.components import render_page_header

def render_summary():
    render_page_header("Summary generator","Create concise revision notes from your uploaded material.")
    materials=get_all_materials()
    if not materials: st.info("Upload material first."); return
    options={f'{m["filename"]} · {m["subject"]}':m["id"] for m in materials}
    choice=st.selectbox("Choose material",list(options.keys())); num_sentences=st.slider("Summary length",3,10,5)
    if st.button("Generate summary",type="primary"):
        material=get_material_by_id(options[choice])
        with st.spinner("Generating summary..."): summary=generate_summary(material["extracted_text"],num_sentences)
        st.markdown('<div class="sw-panel"><h3>📝 Your summary</h3></div>',unsafe_allow_html=True); st.write(summary)
