import streamlit as st

CUSTOM_CSS = """
<style>
:root { --sage:#71866a; --sage-dark:#52654d; --ink:#20251f; --muted:#687067; --line:#e5e8e2; --surface:#ffffff; --soft:#f5f7f2; --peach:#f7e9dc; }
.stApp { background:#f8f9f6; color:var(--ink); }
.block-container { max-width:1180px; padding-top:2.2rem; padding-bottom:3rem; }
section[data-testid="stSidebar"] { background:#fff; border-right:1px solid var(--line); }
section[data-testid="stSidebar"] .block-container { padding:1.5rem 1rem; }
section[data-testid="stSidebar"] [data-testid="stRadio"] label { border-radius:12px; padding:.45rem .55rem; color:#4c544b; }
section[data-testid="stSidebar"] [data-testid="stRadio"] label:hover { background:#f1f4ee; }
.stButton > button { border-radius:11px; border:1px solid var(--sage); background:var(--sage); color:white; font-weight:650; padding:.58rem 1rem; transition:.15s ease; }
.stButton > button:hover { background:var(--sage-dark); border-color:var(--sage-dark); transform:translateY(-1px); }
.stTextInput input, .stSelectbox [data-baseweb="select"], .stFileUploader section, .stSlider { border-radius:12px; }
.sw-brand { padding:.35rem .2rem 1rem; }
.sw-brand h2 { margin:0; color:var(--ink); font-size:1.25rem; }
.sw-brand p { margin:.25rem 0 0; color:var(--muted); font-size:.82rem; }
.sw-hero { background:linear-gradient(135deg,#fff 0%,#f2f6ef 100%); border:1px solid var(--line); border-radius:24px; padding:2.4rem 2.5rem; margin-bottom:1.6rem; box-shadow:0 8px 30px rgba(32,37,31,.05); }
.sw-hero h1 { margin:0 0 .65rem; font-size:2.45rem; letter-spacing:-.04em; color:var(--ink); }
.sw-hero p { margin:0; max-width:720px; color:var(--muted); font-size:1.05rem; line-height:1.65; }
.sw-section { display:flex; align-items:center; justify-content:space-between; margin:1.4rem 0 .8rem; }
.sw-section h2 { margin:0; font-size:1.25rem; color:var(--ink); }
.sw-section p { margin:.2rem 0 0; color:var(--muted); font-size:.88rem; }
.card { background:var(--surface); border:1px solid var(--line); border-radius:18px; padding:1.25rem; margin-bottom:1rem; box-shadow:0 5px 18px rgba(32,37,31,.045); min-height:120px; transition:.16s ease; }
.card:hover { transform:translateY(-2px); box-shadow:0 10px 25px rgba(32,37,31,.08); border-color:#d5dbd1; }
.card h3 { margin:0 0 .55rem; color:var(--ink); font-size:1.02rem; }
.card p { margin:0; color:var(--muted); line-height:1.55; font-size:.9rem; }
.card .sw-card-icon { font-size:1.5rem; margin-bottom:.65rem; }
.metric-card { background:#fff; border:1px solid var(--line); border-radius:18px; padding:1.15rem 1.25rem; box-shadow:0 5px 18px rgba(32,37,31,.045); }
.metric-card .metric-icon { font-size:1.25rem; }
.metric-card h2 { margin:.35rem 0 0; color:var(--ink); font-size:2rem; letter-spacing:-.03em; }
.metric-card p { margin:.15rem 0 0; color:var(--muted); font-size:.82rem; }
.sw-tip { background:var(--peach); border:1px solid #eed8c4; border-radius:18px; padding:1rem 1.15rem; margin-top:1.4rem; }
.sw-tip-title { font-weight:700; color:#5e4937; margin-bottom:.2rem; }
.sw-tip-text { color:#756252; font-size:.88rem; }
.sw-page-head { margin-bottom:1.35rem; }
.sw-page-head h1 { margin:0; color:var(--ink); font-size:2rem; letter-spacing:-.03em; }
.sw-page-head p { margin:.35rem 0 0; color:var(--muted); }
.sw-panel { background:#fff; border:1px solid var(--line); border-radius:18px; padding:1.25rem; box-shadow:0 5px 18px rgba(32,37,31,.04); margin-bottom:1rem; }
.sw-panel h3 { margin:0 0 .65rem; color:var(--ink); }
.sw-item { background:#fff; border:1px solid var(--line); border-radius:15px; padding:.9rem 1rem; margin-bottom:.65rem; }
.sw-item-title { font-weight:700; color:var(--ink); }
.sw-item-meta { color:var(--muted); font-size:.82rem; margin-top:.2rem; }
.sw-empty { text-align:center; background:#fff; border:1px dashed #cfd6cb; border-radius:18px; padding:2rem; color:var(--muted); }
.sw-score { background:#f2f6ef; border:1px solid #dce5d8; border-radius:20px; padding:1.4rem; text-align:center; margin-bottom:1.2rem; }
.sw-score .big { font-size:2.6rem; font-weight:800; color:var(--sage-dark); }
.sw-score .label { color:var(--muted); font-size:.9rem; }
.sw-footer { text-align:center; color:#8a9188; font-size:.78rem; margin-top:2.5rem; padding-top:1rem; border-top:1px solid var(--line); }
</style>
"""

def apply_custom_css():
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
