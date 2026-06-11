import streamlit as st
import pandas as pd
import plotly.express as px
import os
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh
PRIMARY = "#22C55E"      # Green
SECONDARY = "#06B6D4"    # Cyan
CARD = "#0F172A"         # Card Background
BG = "#020617"           # Main Background
TEXT = "#FFFFFF"         # White Text

st.set_page_config(
    page_title="Smart Agriculture Monitoring System",
    page_icon="🌱",
    layout="wide"
)
st_autorefresh(
    interval=5000,
    key="refresh"
)

st.markdown(f"""
<style>

/* =========================
   GLOBAL THEME
========================= */

.stApp {{
    background:{BG};
    color:{TEXT};
}}

.block-container {{
    padding-top:1rem;
    padding-bottom:1rem;
}}

/* =========================
   SIDEBAR
========================= */

[data-testid="stSidebar"] {{
    background:{CARD};
    border-right:1px solid #1E293B;
}}

[data-testid="stSidebar"] * {{
    color:{TEXT};
}}

/* Sidebar Radio Buttons */

div[role="radiogroup"] label {{
    background:#111827;
    border-radius:12px;
    padding:10px;
    margin-bottom:6px;
    border:1px solid #1F2937;
}}

div[role="radiogroup"] label:hover {{
    border:1px solid {PRIMARY};
    transition:0.3s;
}}

/* =========================
   SELECTBOX
========================= */

div[data-baseweb="select"] > div {{
    background:#111827 !important;
    border:2px solid {PRIMARY} !important;
    border-radius:15px !important;
    color:white !important;

    box-shadow:
        0 0 10px rgba(34,197,94,0.20),
        0 0 20px rgba(34,197,94,0.08);
}}

div[data-baseweb="select"] > div:hover {{
    border:2px solid {SECONDARY} !important;

    box-shadow:
        0 0 15px rgba(6,182,212,0.35),
        0 0 30px rgba(6,182,212,0.12);
}}

div[data-baseweb="select"] span {{
    color:white !important;
}}

/* =========================
   HEADINGS
========================= */

h1,h2,h3,h4,h5,h6 {{
    color:{TEXT};
}}

/* =========================
   METRIC CARDS
========================= */

[data-testid="metric-container"] {{
    background:{CARD};
    border:1px solid #1E293B;
    border-left:4px solid {PRIMARY};
    padding:18px;
    border-radius:18px;

    box-shadow:
        0px 0px 12px rgba(34,197,94,0.08);
}}

[data-testid="metric-container"]:hover {{
    border-left:4px solid {SECONDARY};

    box-shadow:
        0px 0px 18px rgba(6,182,212,0.12);

    transition:0.3s;
}}

[data-testid="stMetricValue"] {{
    color:white;
    font-size:30px;
    font-weight:bold;
}}

[data-testid="stMetricLabel"] {{
    color:#9CA3AF;
}}

/* =========================
   CUSTOM DASHBOARD CARDS
========================= */

.dashboard-card {{
    background:{CARD};
    border:1px solid #1E293B;
    border-left:5px solid {PRIMARY};
    border-radius:20px;
    padding:20px;
    margin-bottom:15px;

    box-shadow:
        0px 0px 15px rgba(34,197,94,0.08);
}}

.dashboard-card:hover {{
    border-left:5px solid {SECONDARY};

    box-shadow:
        0px 0px 20px rgba(6,182,212,0.15);

    transition:0.3s;
}}

/* =========================
   DATAFRAME
========================= */

[data-testid="stDataFrame"] {{
    border-radius:15px;
    overflow:hidden;
}}

/* =========================
   BUTTONS
========================= */

.stButton > button {{
    background:{PRIMARY};
    color:white;
    border:none;
    border-radius:12px;
}}

.stButton > button:hover {{
    background:{SECONDARY};
}}

/* =========================
   DOWNLOAD BUTTON
========================= */

.stDownloadButton > button {{
    background:{PRIMARY};
    color:white;
    border:none;
    border-radius:12px;
}}

.stDownloadButton > button:hover {{
    background:{SECONDARY};
}}

</style>
""", unsafe_allow_html=True)

with st.sidebar:

    st.title("🌱 AgriSense AI")

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Analytics",
            "AI Advisor",
            "Data Logs"
        ]
    )

    time_filter = st.selectbox(
        "⏱ Time Range",
        [
            "Last Hour",
            "Last Day",
            "All Data"
        ]
    )

    st.markdown("---")

    st.markdown("""
    🛰️ ESP32

    🌡️ DHT22

    ☁️ ThingSpeak

    📊 Streamlit

    🤖 AI Analytics

    ⚡ Automation
    """)

st.markdown("""
# 🌱 AgriSense AI Platform

### Smart Agriculture Intelligence Platform

📡 Real-Time Monitoring | ☁️ Cloud Analytics | 💧 Smart Irrigation | 🤖 AI Decision Support
""")



st.success("🎉 Welcome to Smart Agriculture Intelligence Platform")

st.markdown("### Real-Time IoT Monitoring Dashboard")

csv_file = os.path.join("data", "sensor_logs.csv")

if not os.path.exists(csv_file):
    st.error("No sensor data found!")
    st.stop()

df = pd.read_csv(csv_file)

latest = df.iloc[-1]
st.caption(
    f"🕒 Last Updated: {latest['Timestamp']}"
)


st.subheader("📈 Real-Time Performance Metrics")

avg_temp = round(df["Temperature"].mean(), 1)

avg_hum = round(df["Humidity"].mean(), 1)

pump_runtime = round(
    (
        len(df[df["Pump"] == "ON"])
        /
        len(df)
    ) * 100,
    1
)

alerts_count = 0

if latest["Temperature"] > 35:
    alerts_count += 1

if latest["Soil"] < 2000:
    alerts_count += 1

if latest["Water"] < 1000:
    alerts_count += 1

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric(
    "🌡 Avg Temp",
    f"{avg_temp}°C"
)

c2.metric(
    "💧 Avg Humidity",
    f"{avg_hum}%"
)

c3.metric(
    "⚙ Pump Runtime",
    f"{pump_runtime}%"
)

c4.metric(
    "🚨 Alerts",
    alerts_count
)
c5.metric(
    "📡 Records",
    len(df)
)

st.markdown(
"""
<div class="dashboard-card">
""",
unsafe_allow_html=True
)

# ==========================
# KPI CARDS
# ==========================

st.markdown("## 🎯 Executive Overview")


col1, col2, col3, col4, col5 = st.columns(5)

farm_health = 100

if latest["Soil"] < 2000:
    farm_health -= 20

if latest["Water"] < 1000:
    farm_health -= 15

if latest["Temperature"] > 35:
    farm_health -= 10

col1.metric("🌱 Farm Health", f"{farm_health}%")
col2.metric("🌡 Temperature", f"{latest['Temperature']}°C")
col3.metric("💧 Humidity", f"{latest['Humidity']}%")
col4.metric("🚰 Water Tank", latest["Water"])
col5.metric("⚙️ Pump", latest["Pump"])



if farm_health >= 85:
    st.success("🟢 Farm Status: Healthy")

elif farm_health >= 60:
    st.warning("🟡 Farm Status: Needs Attention")

else:
    st.error("🔴 Farm Status: Critical")

alerts = 0

if latest["Temperature"] > 35:
    alerts += 1

if latest["Soil"] < 2000:
    alerts += 1

if latest["Water"] < 1000:
    alerts += 1

st.metric("🚨 Active Alerts", alerts)    

col1,col2,col3,col4 = st.columns(4)

col1.info("☀ Sunny")
col2.info("💨 Wind Normal")
col3.info("🌧 Rain Risk Low")
col4.info("🌡 Summer Season")

st.dataframe(
    df.tail(5),
    use_container_width=True
)

with open(csv_file, "rb") as file:

    st.download_button(
        label="📥 Download Sensor Report",
        data=file,
        file_name="sensor_logs.csv",
        mime="text/csv"
    )

           

st.markdown(
"""
</div>
""",
unsafe_allow_html=True
)

# ==========================
# ALERTS
# ==========================

st.subheader("🚨 Alert Center")

if latest["Soil"] < 2000:
    st.warning("💧 Soil Moisture Critical")

if latest["Water"] < 1000:
    st.error("🚰 Water Tank Low")

if latest["Temperature"] > 35:
    st.error("🔥 High Temperature Detected")


st.subheader("⚙️ Pump Status")

if latest["Pump"] == "ON":
    st.success("🟢 Irrigation Pump Active")
else:
    st.error("🔴 Irrigation Pump Inactive")     

# ==========================
# HEALTH STATUS
# ==========================

colA, colB = st.columns(2)

with colA:
    st.subheader("🌱 Soil Health Status")

    if latest["Soil"] < 1500:
        st.error("Dry Soil")
    elif latest["Soil"] < 3000:
        st.warning("Moderate Moisture")
    else:
        st.success("Healthy Soil")

with colB:
    st.subheader("🚰 Water Tank Status")

    if latest["Water"] < 1000:
        st.error("Low Water Level")
    elif latest["Water"] < 2500:
        st.warning("Medium Water Level")
    else:
        st.success("Tank Full")


# ==========================
# PUMP STATUS
# ==========================

if latest["Pump"]=="ON":
    st.success("🟢 Irrigation Pump Active")

else:
    st.error("🔴 Irrigation Pump Inactive")

col1,col2,col3 = st.columns(3)

with col1:
    st.info("🌞 Weather: Sunny")

with col2:
    st.info("🌬 Wind: Normal")

with col3:
    st.info("🌦 Rain Risk: Low")    



st.subheader("⚙ Pump Status")

if latest["Pump"] == "ON":
    st.success("Pump Running")
else:
    st.info("Pump Stopped")

st.divider()

# ==========================
# CHARTS
# ==========================
col1, col2 = st.columns(2)

with col1:

    fig_gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=farm_health,
            title={"text":"🌱 Farm Health"},
            gauge={
                "axis":{"range":[0,100]},
                "bar":{"color":"lime"},
                "steps":[
                    {"range":[0,50],"color":"#7f1d1d"},
                    {"range":[50,80],"color":"#78350f"},
                    {"range":[80,100],"color":"#14532d"}
                ]
            }
        )
    )

    st.plotly_chart(
        fig_gauge,
        use_container_width=True
    )
    
     

with col2:

    pump_counts = df["Pump"].value_counts()

    fig_pump = px.pie(
        names=pump_counts.index,
        values=pump_counts.values,
        hole=0.7,
        title="⚙ Pump Utilization"
       
    )
    
   

    st.plotly_chart(
        fig_pump,
        use_container_width=True
    )

st.markdown(
"""
<div class="dashboard-card">
""",
unsafe_allow_html=True
)


   
st.subheader("📈 Sensor Analytics")
fig_temp = px.area(
    df,
    y="Temperature",
    title="Temperature Analytics"
)

fig_temp.update_layout(
    paper_bgcolor="#0B1120",
    plot_bgcolor="#0B1120",
    font_color="white"
)



fig_hum = px.area(
    df,
    y="Humidity",
    title="Humidity Analytics"
)

fig_temp.update_layout(
    paper_bgcolor=BG,
    plot_bgcolor=BG,
    font_color=TEXT
)

fig_temp.update_layout(
    paper_bgcolor="#0B1120",
    plot_bgcolor="#0B1120",
    font_color="white"
)

fig_soil = px.area(
    df,
    y="Soil",
    title="Soil Moisture Analytics"
)

fig_temp.update_layout(
    paper_bgcolor="#0B1120",
    plot_bgcolor="#0B1120",
    font_color="white"
)


fig_water = px.area(
    df,
    y="Water",
    title="Water Tank Analytics"
)

fig_temp.update_layout(
    paper_bgcolor="#0B1120",
    plot_bgcolor="#0B1120",
    font_color="white"
)




col1,col2 = st.columns(2)

with col1:
    st.plotly_chart(fig_temp,use_container_width=True)

with col2:
    st.plotly_chart(fig_hum,use_container_width=True)

with col1:
    st.plotly_chart(fig_soil,use_container_width=True)

with col2:
    st.plotly_chart(fig_water,use_container_width=True)

st.markdown(
"""
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class="dashboard-card">
""",
unsafe_allow_html=True
)


st.subheader("🤖 AI Farm Advisor")

recommendations = []

if latest["Soil"] < 2000:
    recommendations.append(
        "💧 Irrigation recommended immediately"
    )

if latest["Temperature"] > 35:
    recommendations.append(
        "🌡 Heat stress detected. Monitor crops between 2PM–4PM."
    )

if latest["Water"] > 2000:
    recommendations.append(
        "🚰 Water reserve healthy."
    )

if latest["Pump"] == "OFF":
    recommendations.append(
        "⚙ Pump currently inactive."
    )

for rec in recommendations:
    st.info(rec)

if len(recommendations) == 0:
    st.success("✅ Farm operating optimally")

st.markdown(
"""
</div>
""",
unsafe_allow_html=True
)

# ==========================
# RAW DATA
# ==========================

st.markdown(
"""
<div class="dashboard-card">
""",
unsafe_allow_html=True
)


st.subheader("📋 Sensor Data Logs")
st.dataframe(df, use_container_width=True)

with st.expander(
    "📚 Smart Farming Insights"
):

    st.info("""
💧 Smart Irrigation saves up to 30% water.

🌱 Continuous monitoring improves crop yield.

📡 IoT enables remote farming.

⚡ Automation reduces labor costs.
""")
    
st.markdown(
"""
</div>
""",
unsafe_allow_html=True
)    



st.markdown("---")

st.markdown("""
## 👨‍💻 Developed By

### Sujal Kumar Shaw

🎓 B.Tech Student

📡 IoT • Embedded Systems • Data Analytics

🌱 IoT Smart Agriculture Intelligence Platform

🚀 Real-Time Monitoring | Smart Irrigation | Cloud Analytics
""")