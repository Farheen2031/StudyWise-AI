import streamlit as st
from pdf_utils.pdf_processor import extract_text_from_pdf, get_page_count
from database.db_handler import add_material
from ui.components import SUBJECTS


def render_upload():
    st.title("📤 Upload Study Material")

    subject = st.selectbox("Select Subject", SUBJECTS)
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        if st.button("Process and Save"):
            with st.spinner("Extracting text from PDF..."):
                text = extract_text_from_pdf(uploaded_file)

                uploaded_file.seek(0)
                pages = get_page_count(uploaded_file)

            if not text:
                st.error(
                    "Couldn't extract text. Make sure this is a "
                    "text-based PDF, not a scanned image."
                )
            else:
                material_id = add_material(
                    subject,
                    uploaded_file.name,
                    text,
                    pages
                )

                st.success(
                    f"Saved! '{uploaded_file.name}' added under "
                    f"{subject} (ID: {material_id})"
                )

                st.write(
                    f"Extracted {len(text)} characters from "
                    f"{pages} pages."
                )
