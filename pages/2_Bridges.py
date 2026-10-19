import streamlit as st
import pandas as pd
import plotly.express as px

# NOTE: st.set_page_config is removed because it is handled in app.py

st.markdown('# 🌉 Bridge Monitoring')
st.caption('Structural health analysis • CNN + LSTM • DEMO DATA')
st.info('Prototype page. Replace the example values with outputs from your bridge model.')

a,b,c,d=st.columns(4)
a.metric('Average health score','88/100')
b.metric('Bridges monitored','08')
c.metric('Active alerts','01')
d.metric('Model','CNN + LSTM')

df=pd.DataFrame({'Bridge':['B-01','B-02','B-03','B-04'],'Health':[94,76,91,88],'Risk':['Low','Medium','Low','Low']})
fig=px.bar(df,x='Bridge',y='Health',color='Risk',range_y=[0,100],color_discrete_map={'Low':'#22d3a6','Medium':'#f6bd4f','High':'#ff647c'})
fig.update_layout(template='plotly_dark')
st.plotly_chart(fig,use_container_width=True)

st.dataframe(pd.DataFrame({
    'Bridge':['B-01','B-02','B-03'],
    'Vibration RMS (mm/s)':[1.7,4.8,2.2],
    'Strain (με)':[120,245,136],
    'Deflection (mm)':[3.1,7.8,3.8],
    'Prediction':['Normal','Unusual vibration','Normal']
}),use_container_width=True,hide_index=True)

# The st.page_link is removed because st.navigation handles this automatically
