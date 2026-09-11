import streamlit as st
from database.db_handler import get_all_materials, delete_material
from ui.components import render_card


def render_materials():
    st.title("📚 Your Materials")
    materials = get_all_materials()

    if not materials:
        st.info("No materials yet. Go to Upload to add your first PDF.")
        return

    subjects = sorted(set(m["subject"] for m in materials))
    filter_subject = st.selectbox("Filter by subject", ["All"] + subjects)

    for m in materials:
        if filter_subject != "All" and m["subject"] != filter_subject:
            continue

        col1, col2 = st.columns([4, 1])

        with col1:
            render_card(
                m["filename"],
                f"Subject: {m['subject']} | "
                f"Uploaded: {m['upload_date']} | "
                f"Pages: {m['page_count']}",
                "📄"
            )

        with col2:
            if st.button("Delete", key=f"del_{m['id']}"):
                delete_material(m["id"])
                st.rerun()