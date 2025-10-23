# import streamlit as st
# from PIL import Image
# import base64
# import threading
# import paho.mqtt.client as mqtt
# import time

# # ------------------ PAGE SETTINGS ------------------
# st.set_page_config(layout="wide", page_title="VR Cycling")

# # ------------------ FUNCTIONS ------------------
# def get_base64_of_bin_file(bin_file):
#     """Convert local image file to base64 string"""
#     with open(bin_file, "rb") as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# # ------------------ MQTT CONFIGURATION ------------------
# BROKER = "18.140.19.253"
# PORT = 8090
# USERNAME = "bikeuser"
# PASSWORD = "DYuKE42w8CoSDyb0HN46Blkk9XSfY8Z9zes6Ek6eA"
# TOPICS = [("VRcycling/UserA/HIncTime", 0), ("VRcycling/UserA/GIncTime", 0)]

# mqtt_data = {"HIncTime": 0, "GIncTime": 0}

# def on_connect(client, userdata, flags, rc):
#     if rc == 0:
#         client.subscribe(TOPICS)
#     else:
#         print(f"Connection failed: {rc}")

# def on_message(client, userdata, msg):
#     topic = msg.topic
#     payload = msg.payload.decode("utf-8")
#     try:
#         value = int(payload)
#         value = max(0, min(301, value))  # Clamp between 0–301
#         if topic.endswith("HIncTime"):
#             mqtt_data["HIncTime"] = value
#         elif topic.endswith("GIncTime"):
#             mqtt_data["GIncTime"] = value
#     except ValueError:
#         pass  # Ignore non-numeric payloads

# def mqtt_loop():
#     client = mqtt.Client()
#     client.username_pw_set(USERNAME, PASSWORD)
#     client.on_connect = on_connect
#     client.on_message = on_message
#     client.connect(BROKER, PORT, 60)
#     client.loop_forever()

# threading.Thread(target=mqtt_loop, daemon=True).start()

# # ------------------ IMAGE FILES ------------------
# background_image_path = "images/background.jpg"
# background_base64 = get_base64_of_bin_file(background_image_path)

# # ------------------ CUSTOM CSS ------------------
# st.markdown(f"""
#     <style>
#     [data-testid="stAppViewContainer"] {{
#         background-image: url("data:image/jpg;base64,{background_base64}");
#         background-size: cover;
#         background-position: center;
#         background-repeat: no-repeat;
#     }}
#     .box {{
#         background-color: rgba(255, 255, 255, 0.8);
#         padding: 20px 25px;
#         border-radius: 15px;
#         box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
#         margin-bottom: 20px;
#         color: #000000;
#     }}
#     .subheader {{
#         font-size: 1.4rem;
#         font-weight: 600;
#         color: #222;
#         background-color: rgba(240, 240, 240, 0.8);
#         border-radius: 12px;
#         padding: 10px 15px;
#         text-align: center;
#         margin-bottom: 15px;
#         box-shadow: 0 3px 8px rgba(0, 0, 0, 0.3);
#     }}
#     .progress-bar {{
#         position: relative;
#         width: 90%;
#         height: 10px;
#         background: rgba(0,0,0,0.15);
#         border-radius: 5px;
#         margin: 30px auto;
#     }}
#     .pointer {{
#         position: absolute;
#         top: -7px;
#         width: 20px;
#         height: 20px;
#         border-radius: 50%;
#         background-color: #3498db;
#         transition: left 0.5s ease-in-out;
#         box-shadow: 0 0 6px rgba(0,0,0,0.3);
#     }}
#     .pointer2 {{
#         background-color: #e74c3c;
#     }}
#     </style>
# """, unsafe_allow_html=True)

# # ------------------ LAYOUT ------------------
# col1, col2 = st.columns(2)

# with col1:
#     st.markdown('<div class="subheader">🚴 VR Cycling ...</div>', unsafe_allow_html=True)

#     paragraph_en = """This is a sample paragraph in English. 
#     It represents the same content translated into different languages."""
#     paragraph_si = """මෙය ඉංග්‍රීසි පාඨයේ සිංහල පරිවර්තනයකි. 
#     එකම අන්තර්ගතය විවිධ භාෂාවලින් නිරූපණය කරයි."""
#     paragraph_ta = """இது ஆங்கில பத்தி தமிழ் மொழிபெயர்ப்பு ஆகும். 
#     அதே உள்ளடக்கத்தை வேறு மொழிகளில் வெளிப்படுத்துகிறது."""

#     st.markdown(f'<div class="box"><b>English:</b><br>{paragraph_en}</div>', unsafe_allow_html=True)
#     st.markdown(f'<div class="box"><b>සිංහල:</b><br>{paragraph_si}</div>', unsafe_allow_html=True)
#     st.markdown(f'<div class="box"><b>தமிழ்:</b><br>{paragraph_ta}</div>', unsafe_allow_html=True)

# with col2:
#     st.markdown('<div class="subheader">About This Section</div>', unsafe_allow_html=True)
#     st.markdown(
#         '<div class="box">This section displays some text at the top and dynamic MQTT visual below it.</div>',
#         unsafe_allow_html=True
#     )

#     st.markdown('<div class="subheader">Live MQTT Visual</div>', unsafe_allow_html=True)
#     bar_placeholder = st.empty()

# # ------------------ DISPLAY LOOP ------------------
# while True:
#     h_value = mqtt_data["HIncTime"]
#     g_value = mqtt_data["GIncTime"]

#     # Convert 0–301 to percentage
#     h_pos = (h_value / 301) * 100
#     g_pos = (g_value / 301) * 100

#     html_content = f"""
#     <div class="box">
#         <div class="progress-bar">
#             <div class="pointer" style="left:{h_pos}%;"></div>
#             <div class="pointer pointer2" style="left:{g_pos}%;"></div>
#         </div>
#         <b>HIncTime:</b> {h_value} &nbsp;&nbsp; | &nbsp;&nbsp; <b>GIncTime:</b> {g_value}
#     </div>
#     """

#     bar_placeholder.markdown(html_content, unsafe_allow_html=True)
#     time.sleep(1)






















import streamlit as st
from PIL import Image
import base64
import threading
import paho.mqtt.client as mqtt
import time
import numpy as np
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh

# ------------------ PAGE SETTINGS ------------------
st.set_page_config(layout="wide", page_title="VR Cycling")

# ------------------ FUNCTIONS ------------------
def get_base64_of_bin_file(bin_file):
    """Convert local image file to base64 string"""
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# ------------------ MQTT CONFIGURATION ------------------
BROKER = "18.140.19.253"
PORT = 8090
USERNAME = "bikeuser"
PASSWORD = "DYuKE42w8CoSDyb0HN46Blkk9XSfY8Z9zes6Ek6eA"
TOPICS = [("VRcycling/UserA/HIncTime", 0), ("VRcycling/UserA/GIncTime", 0)]

mqtt_data = {"HIncTime": 0, "GIncTime": 0}

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe(TOPICS)
    else:
        print(f"Connection failed: {rc}")

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode("utf-8")
    try:
        value = int(payload)
        value = max(0, min(301, value))  # Clamp between 0–301
        if topic.endswith("HIncTime"):
            mqtt_data["HIncTime"] = value
        elif topic.endswith("GIncTime"):
            mqtt_data["GIncTime"] = value
    except ValueError:
        pass  # Ignore non-numeric payloads

def mqtt_loop():
    client = mqtt.Client()
    client.username_pw_set(USERNAME, PASSWORD)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)
    client.loop_forever()

threading.Thread(target=mqtt_loop, daemon=True).start()

# ------------------ IMAGE FILES ------------------
background_image_path = "images/background.jpg"
background_base64 = get_base64_of_bin_file(background_image_path)

# ------------------ CUSTOM CSS ------------------
st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/jpg;base64,{background_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    .box {{
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px 25px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        margin-bottom: 20px;
        color: #000000;
    }}
    .subheader {{
        font-size: 1.4rem;
        font-weight: 600;
        color: #222;
        background-color: rgba(240, 240, 240, 0.8);
        border-radius: 12px;
        padding: 10px 15px;
        text-align: center;
        margin-bottom: 15px;
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.3);
    }}
    </style>
""", unsafe_allow_html=True)

# ------------------ LAYOUT ------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="subheader">🚴 VR Cycling ...</div>', unsafe_allow_html=True)

    paragraph_en = """This is a sample paragraph in English. 
    It represents the same content translated into different languages."""
    paragraph_si = """මෙය ඉංග්‍රීසි පාඨයේ සිංහල පරිවර්තනයකි. 
    එකම අන්තර්ගතය විවිධ භාෂාවලින් නිරූපණය කරයි."""
    paragraph_ta = """இது ஆங்கில பத்தி தமிழ் மொழிபெயர்ப்பு ஆகும். 
    அதே உள்ளடக்கத்தை வேறு மொழிகளில் வெளிப்படுத்துகிறது."""

    st.markdown(f'<div class="box"><b>English:</b><br>{paragraph_en}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="box"><b>සිංහල:</b><br>{paragraph_si}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="box"><b>தமிழ்:</b><br>{paragraph_ta}</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="subheader">About This Section</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="box">This section displays some text at the top and dynamic MQTT visual below it.</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="subheader">Live MQTT Path</div>', unsafe_allow_html=True)
    plot_placeholder = st.empty()

# ------------------ LOAD PATH DATA ------------------
try:
    path_data = np.loadtxt("GregoryPathData.txt", delimiter=",")  # lat,long per line
    lats, longs = path_data[:, 0], path_data[:, 1]

    # Normalize to fit visually
    lats = (lats - np.min(lats)) / (np.max(lats) - np.min(lats))
    longs = (longs - np.min(longs)) / (np.max(longs) - np.min(longs))

    # Interpolate to 302 points (0–301)
    indices = np.linspace(0, len(lats) - 1, 302)
    interp_lats = np.interp(indices, np.arange(len(lats)), lats)
    interp_longs = np.interp(indices, np.arange(len(longs)), longs)

except Exception as e:
    st.error(f"Error loading GregoryPathData.txt: {e}")
    st.stop()

# ------------------ FUNCTION TO DRAW PATH ------------------
def plot_path(h_value, g_value):
    fig = go.Figure()

    # Draw the path
    fig.add_trace(go.Scatter(
        x=interp_longs,
        y=interp_lats,
        mode="lines",
        line=dict(color="gray", width=4),
        name="Path"
    ))

    # HIncTime pointer
    fig.add_trace(go.Scatter(
        x=[interp_longs[h_value]],
        y=[interp_lats[h_value]],
        mode="markers",
        marker=dict(color="blue", size=15),
        name="HIncTime"
    ))

    # GIncTime pointer
    fig.add_trace(go.Scatter(
        x=[interp_longs[g_value]],
        y=[interp_lats[g_value]],
        mode="markers",
        marker=dict(color="red", size=15),
        name="GIncTime"
    ))

    fig.update_layout(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False, scaleanchor="x", scaleratio=1),
        showlegend=False,
        margin=dict(l=0, r=0, t=0, b=0),
        height=400,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)"
    )

    return fig

# ------------------ DISPLAY LOOP ------------------
# Refresh every 1000 milliseconds (1 second)
st_autorefresh(interval=1000, key="mqtt_refresh")

# Read the latest MQTT data
h_value = int(np.clip(mqtt_data["HIncTime"], 0, 301))
g_value = int(np.clip(mqtt_data["GIncTime"], 0, 301))

# Plot the figure
fig = plot_path(h_value, g_value)
plot_placeholder.plotly_chart(fig, use_container_width=True)
