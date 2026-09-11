import streamlit as st
from database.db_handler import get_all_materials, get_material_by_id
from ai_features.summary_generator import generate_summary


def render_summary():
    st.title("📝 Summary Generator")

    materials = get_all_materials()

    if not materials:
        st.info("Upload material first.")
        return

    options = {
        f"{m['filename']} ({m['subject']})": m["id"]
        for m in materials
    }

    choice = st.selectbox("Choose material", list(options.keys()))

    num_sentences = st.slider(
        "Summary length (sentences)",
        3,
        10,
        5
    )

    if st.button("Generate Summary"):
        material = get_material_by_id(options[choice])

        with st.spinner("Generating summary..."):
            summary = generate_summary(
                material["extracted_text"],
                num_sentences
            )

        st.markdown("### Summary")
        st.write(summary)