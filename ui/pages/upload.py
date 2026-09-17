import streamlit as st
from pdf_utils.pdf_processor import extract_text_from_pdf, get_page_count
from database.db_handler import add_material
from ui.components import SUBJECTS, render_page_header

def render_upload():
    render_page_header("Upload study material","Add a PDF and organize it by subject.")
    st.markdown('<div class="sw-panel"><h3>📤 Add a new PDF</h3><p style="color:#687067">Text-based PDFs work best because StudyWise AI extracts their text locally.</p></div>',unsafe_allow_html=True)
    subject=st.selectbox("Select subject",SUBJECTS)
    uploaded_file=st.file_uploader("Choose a PDF file",type="pdf")
    if uploaded_file is not None:
        st.markdown(f'<div class="sw-item"><div class="sw-item-title">📄 {uploaded_file.name}</div><div class="sw-item-meta">Ready to process · {uploaded_file.size/1024:.1f} KB</div></div>',unsafe_allow_html=True)
        if st.button("Process and save",type="primary"):
            with st.spinner("Extracting text from PDF..."):
                text=extract_text_from_pdf(uploaded_file); uploaded_file.seek(0); pages=get_page_count(uploaded_file)
            if not text: st.error("Couldn’t extract text. Make sure this is a text-based PDF, not a scanned image.")
            else:
                material_id=add_material(subject,uploaded_file.name,text,pages)
                st.success(f"Saved! {uploaded_file.name} was added under {subject}.")
                st.write(f"Extracted {len(text)} characters from {pages} pages.")
