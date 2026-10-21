import streamlit as st

st.markdown("# ⚡ InfraPulse")
st.markdown("### Infrastructure monitoring prototype")
st.write(
    "InfraPulse brings railway, bridge, and dam monitoring concepts into one interface. "
    "The prototype presents sample condition indicators and anomaly results to help users "
    "review infrastructure status and prioritize where a human inspection may be needed."
)

st.warning(
    "DEMO MODE — all readings, health scores, alerts, and predictions are synthetic. "
    "This prototype is not connected to sensors or trained models and must not be used "
    "to make real-world safety decisions."
)

st.markdown("## Explore the monitoring pages")
railway, bridges, dams = st.columns(3)

with railway:
    st.markdown("### 🚆 Railway")
    st.write("View sample track health, vibration, temperature, alignment, speed, and anomaly results.")
    st.page_link(
        "pages/1_Railway.py",
        label="Open Railway Monitoring",
        icon="🚆",
        use_container_width=True,
    )

with bridges:
    st.markdown("### 🌉 Bridges")
    st.write("Review sample bridge health, risk levels, vibration, strain, and deflection.")
    st.page_link(
        "pages/2_Bridges.py",
        label="Open Bridge Monitoring",
        icon="🌉",
        use_container_width=True,
    )

with dams:
    st.markdown("### 🌊 Dams")
    st.write("Review sample dam health, reservoir levels, seepage, and pore pressure.")
    st.page_link(
        "pages/3_Dams.py",
        label="Open Dam Monitoring",
        icon="🌊",
        use_container_width=True,
    )

st.markdown("## Project purpose")
st.write(
    "The goal is to demonstrate how condition data from different infrastructure types "
    "could be presented together, so teams can spot indicators that warrant further review. "
    "In a production system, these example values would be replaced with validated sensor "
    "data and model outputs, with qualified professionals responsible for inspections and decisions."
)

st.caption("InfraPulse Review 2 prototype • Illustrative data only")
