import streamlit as st

# ------------------ PAGE SETTINGS ------------------
st.set_page_config(layout="wide", page_title="Multilingual Page")

# ------------------ CUSTOM CSS ------------------
st.markdown("""
    <style>
    /* Set background image with transparency overlay */
    body {
        background-image: linear-gradient(rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.9)), 
                          url("https://images.unsplash.com/photo-1529078155058-5d716f45d604?auto=format&fit=crop&w=1950&q=80");
        background-size: cover;
        background-position: center;
    }

    /* Rounded white box styling for each text section */
    .box {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px 25px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }

    /* Headings style */
    .subheader {
        font-size: 1.4rem;
        font-weight: 600;
        color: #222;
        background-color: rgba(240, 240, 240, 0.8);
        border-radius: 12px;
        padding: 10px 15px;
        text-align: center;
        margin-bottom: 15px;
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.1);
    }

    /* Center image */
    .center-img {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ LAYOUT ------------------
col1, col2 = st.columns(2)

# ---------- LEFT HALF ----------
with col1:
    st.markdown('<div class="subheader">🗣 Multilingual Paragraphs</div>', unsafe_allow_html=True)

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
    st.markdown('<div class="subheader">📄 About This Section</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="box">This section displays some text at the top and an image below it.</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="center-img">', unsafe_allow_html=True)
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Flag_of_Sri_Lanka.svg/1024px-Flag_of_Sri_Lanka.svg.png",
        caption="Sri Lanka Flag",
        use_container_width=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
