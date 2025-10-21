import streamlit as st
from PIL import Image
import base64

# ------------------ PAGE SETTINGS ------------------
st.set_page_config(layout="wide", page_title="VR Cycling")

# ------------------ FUNCTIONS ------------------
def get_base64_of_bin_file(bin_file):
    """Convert local image file to base64 string"""
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# ------------------ IMAGE FILES ------------------
background_image_path = "images/background.jpg"
circle_image_path = "images/circle.png"

# Encode background image as base64
background_base64 = get_base64_of_bin_file(background_image_path)

# ------------------ CUSTOM CSS ------------------
st.markdown(f"""
    <style>
    /* Full page background */
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/jpg;base64,{background_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}

    /* Rounded white box styling for each text section */
    .box {{
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px 25px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        margin-bottom: 20px;
        color: #000000
    }}

    /* Headings style */
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

    /* Center image */
    .center-img {{
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    /* Make container transparent to see background */
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

    # st.markdown('<div class="center-img">', unsafe_allow_html=True)
    # circle_img = Image.open(circle_image_path)
    # st.image(circle_img, caption="Sri Lanka Flag", width=300)
    # st.markdown('</div>', unsafe_allow_html=True)
