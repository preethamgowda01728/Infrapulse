import streamlit as st

st.set_page_config(page_title="InfraPulse", page_icon="⚡", layout="wide")

pages = {
    "Start here": [
        st.Page(
            "pages/0_Introduction.py",
            title="Introduction",
            icon="📘",
            default=True,
        ),
    ],
    "Monitoring": [
        st.Page("pages/1_Railway.py", title="Railway", icon="🚆"),
        st.Page("pages/2_Bridges.py", title="Bridges", icon="🌉"),
        st.Page("pages/3_Dams.py", title="Dams", icon="🌊"),
    ],
}

selected_page = st.navigation(pages, position="sidebar", expanded=True)
st.markdown(
    """<style>
.stApp{background:linear-gradient(135deg,#06111e,#0a1b2b 60%,#071321);color:#eaf4fc}
[data-testid="stSidebar"]{background:#071421;border-right:1px solid #1d3448}
div[data-testid="stMetric"]{background:#0e2032;border:1px solid #1d3a52;border-radius:14px;padding:14px}
.block-container{padding-top:1.5rem}
</style>""",
    unsafe_allow_html=True,
)
selected_page.run()
