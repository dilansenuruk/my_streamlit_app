import streamlit as st
from PIL import Image
import base64
import threading
import paho.mqtt.client as mqtt
import time

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

# Shared variables for MQTT messages
mqtt_data = {"HIncTime": "Waiting for data...", "GIncTime": "Waiting for data..."}

# MQTT callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe(TOPICS)
    else:
        print(f"Connection failed with code {rc}")

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode("utf-8")
    if topic.endswith("HIncTime"):
        mqtt_data["HIncTime"] = payload
    elif topic.endswith("GIncTime"):
        mqtt_data["GIncTime"] = payload

# MQTT thread function
def mqtt_loop():
    client = mqtt.Client()
    client.username_pw_set(USERNAME, PASSWORD)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)
    client.loop_forever()

# Start MQTT in a background thread
threading.Thread(target=mqtt_loop, daemon=True).start()

# ------------------ IMAGE FILES ------------------
background_image_path = "images/background.jpg"
circle_image_path = "images/circle.png"

# Encode background image as base64
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
        color: #000000
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

    .center-img {{
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    .stApp {{
        background: transparent;
    }}
    </style>
""", unsafe_allow_html=True)

# ------------------ LAYOUT ------------------
col1, col2 = st.columns(2)

# ---------- LEFT HALF ----------
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

# ---------- RIGHT HALF ----------
with col2:
    st.markdown('<div class="subheader">About This Section</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="box">This section displays some text at the top and an image below it.</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="subheader">Live MQTT Data</div>', unsafe_allow_html=True)
    h_inc_placeholder = st.empty()
    g_inc_placeholder = st.empty()

    # Continuous update loop (auto-refresh every 1 second)
    while True:
        h_inc_placeholder.markdown(
            f'<div class="box"><b>VRcycling/UserA/HIncTime:</b> {mqtt_data["HIncTime"]}</div>',
            unsafe_allow_html=True
        )
        g_inc_placeholder.markdown(
            f'<div class="box"><b>VRcycling/UserA/GIncTime:</b> {mqtt_data["GIncTime"]}</div>',
            unsafe_allow_html=True
        )
        time.sleep(1)


    # st.markdown('<div class="center-img">', unsafe_allow_html=True)
    # circle_img = Image.open(circle_image_path)
    # st.image(circle_img, caption="Sri Lanka Flag", width=300)
    # st.markdown('</div>', unsafe_allow_html=True)
