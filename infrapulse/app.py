import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='InfraPulse | Railway Monitoring', page_icon='🚆', layout='wide')
st.markdown('''<style>
.stApp{background:linear-gradient(135deg,#06111e,#0a1b2b 60%,#071321);color:#eaf4fc}
[data-testid="stSidebar"]{background:#071421;border-right:1px solid #1d3448}
div[data-testid="stMetric"]{background:#0e2032;border:1px solid #1d3a52;border-radius:14px;padding:14px}
.block-container{padding-top:1.5rem}
</style>''', unsafe_allow_html=True)
with st.sidebar:
    st.markdown('## ⚡ InfraPulse')
    st.caption('Smarter infrastructure. Safer tomorrow.')
    st.markdown('---')
    st.title("InfraPulse")

    st.page_link("pages/2_Bridges.py", label="Bridges", icon="🌉")
    st.page_link("pages/3_Dams.py", label="Dams", icon="🏗️")
    st.markdown('---')
    st.caption('Review 2 prototype • Demo data only')

st.markdown('# 🚆 Railway Monitoring')
st.markdown('AI-assisted track condition monitoring powered by a **1D-CNN anomaly detection pipeline**.')
st.warning('DEMO MODE — all values below are synthetic sample data, not live sensor readings.')
st.image('https://images.unsplash.com/photo-1474487548417-781cb71495f3?auto=format&fit=crop&w=1800&q=85', caption='Railway corridor — illustrative banner', use_container_width=True)
sections = pd.DataFrame([
 {'Section':'R-03 • North Corridor','Health':92,'Risk':'Low','Vibration RMS (mm/s)':2.1,'Rail temp (°C)':34.2,'Alignment deviation (mm)':1.8,'Speed (km/h)':78,'1D-CNN result':'Normal','Confidence':94},
 {'Section':'R-07 • Central Line','Health':76,'Risk':'Medium','Vibration RMS (mm/s)':5.8,'Rail temp (°C)':39.5,'Alignment deviation (mm)':4.7,'Speed (km/h)':64,'1D-CNN result':'Irregular vibration','Confidence':87},
 {'Section':'R-12 • East Junction','Health':61,'Risk':'High','Vibration RMS (mm/s)':8.2,'Rail temp (°C)':43.1,'Alignment deviation (mm)':7.3,'Speed (km/h)':51,'1D-CNN result':'Track geometry deviation','Confidence':91},
])
section = st.selectbox('Track section', ['All sections'] + sections['Section'].tolist())
shown = sections if section == 'All sections' else sections[sections.Section == section]
health = int(shown.Health.mean())
alerts = int((shown.Risk != 'Low').sum())
anomalies = int((shown['1D-CNN result'] != 'Normal').sum())
st.markdown('### Network health at a glance')
a,b,c,d = st.columns(4)
a.metric('Overall health score', f'{health}/100')
b.metric('Sections monitored', len(shown))
c.metric('Active alerts', alerts)
d.metric('Anomalies detected', anomalies)
st.markdown('### Track condition metrics')
a,b,c,d = st.columns(4)
a.metric('Vibration RMS', f'{shown["Vibration RMS (mm/s)"].mean():.1f} mm/s')
b.metric('Rail temperature', f'{shown["Rail temp (°C)"].mean():.1f} °C')
c.metric('Alignment deviation', f'{shown["Alignment deviation (mm)"].mean():.1f} mm')
d.metric('Avg operating speed', f'{shown["Speed (km/h)"].mean():.0f} km/h')
left,right = st.columns([1.1,1])
with left:
    st.markdown('### Health score by section')
    fig=px.bar(shown,x='Section',y='Health',color='Risk',text='Health',range_y=[0,100],color_discrete_map={'Low':'#22d3a6','Medium':'#f6bd4f','High':'#ff647c'})
    fig.update_layout(template='plotly_dark',paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',xaxis_title='',yaxis_title='Health / 100')
    st.plotly_chart(fig,use_container_width=True)
with right:
    st.markdown('### 1D-CNN anomaly results')
    st.dataframe(shown[['Section','1D-CNN result','Confidence','Risk']],hide_index=True,use_container_width=True)
    st.caption('Replace these example predictions with inference output from your trained 1D-CNN.')
st.markdown('### Health trend • last 7 days')
dates=pd.date_range('2026-10-13',periods=7,freq='D')
trend=pd.DataFrame({'Date':list(dates)*3,'Health score':[94,93,93,92,92,91,92,82,81,79,78,77,75,76,68,66,64,63,62,60,61],'Section':['R-03 • North Corridor']*7+['R-07 • Central Line']*7+['R-12 • East Junction']*7})
if section!='All sections': trend=trend[trend.Section==section]
fig=px.line(trend,x='Date',y='Health score',color='Section',markers=True,color_discrete_sequence=['#35d6e8','#f6bd4f','#ff647c'])
fig.update_layout(template='plotly_dark',paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',yaxis_range=[0,100])
st.plotly_chart(fig,use_container_width=True)
st.markdown('### Recent alerts')
alerts_df=pd.DataFrame([
 {'Severity':'🔴 High','Section':'R-12 • East Junction','Alert':'Track geometry deviation above demo threshold','Time':'19 Oct 2026 • 09:42','Suggested action':'Prioritize field inspection'},
 {'Severity':'🟠 Medium','Section':'R-07 • Central Line','Alert':'Irregular vibration pattern detected by 1D-CNN','Time':'19 Oct 2026 • 08:16','Suggested action':'Schedule targeted inspection'},
 {'Severity':'🟢 Low','Section':'R-03 • North Corridor','Alert':'No significant anomaly detected','Time':'19 Oct 2026 • 07:55','Suggested action':'Continue routine monitoring'},
])
if section!='All sections': alerts_df=alerts_df[alerts_df.Section==section]
st.dataframe(alerts_df,hide_index=True,use_container_width=True)
st.markdown('### Section details')
for _,r in shown.iterrows():
    with st.expander(f'{r.Section} • Health {r.Health}/100 • {r.Risk} risk'):
        x,y,z=st.columns(3); x.metric('1D-CNN prediction',r['1D-CNN result']); y.metric('Confidence',f"{r.Confidence}%"); z.metric('Risk level',r.Risk)
        st.write('Suggested next step:', 'Prioritize field inspection.' if r.Risk=='High' else 'Schedule targeted inspection.' if r.Risk=='Medium' else 'Continue routine monitoring.')
st.caption('InfraPulse Review 2 prototype. All metrics, scores, predictions, and alerts are illustrative sample data.')
