import streamlit as st

SUBJECTS = ["Hindi", "English", "Urdu", "Maths", "Science", "History", "Geography", "Computer Science", "Other"]
NAV_ITEMS = {"🏠 Home":"home","📊 Dashboard":"dashboard","📤 Upload":"upload","📚 Materials":"materials","📝 Summary":"summary","❓ Important Questions":"important_questions","🧠 Quiz":"quiz","🏆 Results":"results"}

def render_page_header(title, subtitle=""):
    st.markdown(f'<div class="sw-page-head"><h1>{title}</h1><p>{subtitle}</p></div>', unsafe_allow_html=True)

def render_card(title, content, icon="📘"):
    st.markdown(f'<div class="card"><div class="sw-card-icon">{icon}</div><h3>{title}</h3><p>{content}</p></div>', unsafe_allow_html=True)

def render_metric_card(value, label, icon="📌"):
    st.markdown(f'<div class="metric-card"><div class="metric-icon">{icon}</div><h2>{value}</h2><p>{label}</p></div>', unsafe_allow_html=True)

def render_item(title, meta, icon="📄"):
    st.markdown(f'<div class="sw-item"><div class="sw-item-title">{icon} {title}</div><div class="sw-item-meta">{meta}</div></div>', unsafe_allow_html=True)

def render_sidebar_nav():
    st.sidebar.markdown('<div class="sw-brand"><h2>📖 StudyWise AI</h2><p>Your smart study workspace</p></div>', unsafe_allow_html=True)
    choice = st.sidebar.radio("", list(NAV_ITEMS.keys()), label_visibility="collapsed")
    st.sidebar.markdown('<div class="sw-footer">Study smarter · Revise better</div>', unsafe_allow_html=True)
    return NAV_ITEMS[choice]
