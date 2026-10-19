import streamlit as st
import pandas as pd
import plotly.express as px

# NOTE: st.set_page_config is removed because it is handled in app.py

st.markdown('# 🌊 Dam Monitoring')
st.caption('Water level, seepage and structural stability • LSTM • DEMO DATA')
st.info('Prototype page. Replace the example values with outputs from your dam model.')

a,b,c,d=st.columns(4)
a.metric('Average health score','95/100')
b.metric('Dams monitored','05')
c.metric('Active alerts','00')
d.metric('Model','LSTM')

df=pd.DataFrame({'Dam':['D-01','D-02','D-03','D-04'],'Health':[97,94,92,96],'Risk':['Low','Low','Low','Low']})
fig=px.bar(df,x='Dam',y='Health',color='Risk',range_y=[0,100],color_discrete_map={'Low':'#22d3a6','Medium':'#f6bd4f','High':'#ff647c'})
fig.update_layout(template='plotly_dark')
st.plotly_chart(fig,use_container_width=True)

st.dataframe(pd.DataFrame({
    'Dam':['D-01','D-02','D-03'],
    'Reservoir level (%)':[78,82,71],
    'Seepage (L/s)':[2.1,3.8,1.9],
    'Pore pressure (kPa)':[124,138,119],
    'Prediction':['Normal','Normal','Normal']
}),use_container_width=True,hide_index=True)

# The st.page_link is removed because st.navigation handles this automatically
