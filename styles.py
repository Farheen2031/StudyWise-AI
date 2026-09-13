"""
styles.py
Custom CSS for a modern, card-based look. Pure CSS — free, no external design service.
"""

import streamlit as st

CUSTOM_CSS = """
<style>
.stApp {
    font-family: 'Segoe UI', sans-serif;
    background-color: #F7F8FC;
}
.card {
    background: white;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    border-left: 5px solid #6C63FF;
}
.card h3 {
    margin-top: 0;
    color: #333;
}
.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4,
.stApp p,
.stApp label {
    color: #222222;
}
.metric-card {
    background: linear-gradient(135deg, #6C63FF, #8B7FFF);
    color: white;
    border-radius: 16px;
    padding: 20px;
    text-align: center;
}
.metric-card h2 {
    margin: 0;
    font-size: 32px;
}
.metric-card p {
    margin: 0;
    opacity: 0.9;
}
</style>
"""


def apply_custom_css():
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)