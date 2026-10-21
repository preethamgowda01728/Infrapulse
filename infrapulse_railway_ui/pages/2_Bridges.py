import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="InfraPulse | Bridges", page_icon="🌉", layout="wide")

st.markdown("# 🌉 Bridge Monitoring")
st.caption("Structural health analysis • CNN + LSTM • DEMO DATA")
st.info("Prototype page. Replace the example values with outputs from your bridge model.")

a, b, c, d = st.columns(4)
a.metric("Average health score", "88/100")
b.metric("Bridges monitored", "08")
c.metric("Active alerts", "01")
d.metric("Model", "CNN + LSTM")

bridges = pd.DataFrame(
    {
        "Bridge": ["B-01", "B-02", "B-03", "B-04"],
        "Health": [94, 76, 91, 88],
        "Risk": ["Low", "Medium", "Low", "Low"],
    }
)

chart = px.bar(
    bridges,
    x="Bridge",
    y="Health",
    color="Risk",
    range_y=[0, 100],
    color_discrete_map={"Low": "#22d3a6", "Medium": "#f6bd4f", "High": "#ff647c"},
)
chart.update_layout(template="plotly_dark")
st.plotly_chart(chart, use_container_width=True)

measurements = pd.DataFrame(
    {
        "Bridge": ["B-01", "B-02", "B-03"],
        "Vibration RMS (mm/s)": [1.7, 4.8, 2.2],
        "Strain (με)": [120, 245, 136],
        "Deflection (mm)": [3.1, 7.8, 3.8],
        "Prediction": ["Normal", "Unusual vibration", "Normal"],
    }
)
st.dataframe(measurements, use_container_width=True, hide_index=True)
st.page_link("app.py", label="← Back to InfraPulse", icon="🏠")
