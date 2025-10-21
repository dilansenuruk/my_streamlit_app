import streamlit as st

# Set the page layout to wide for better horizontal spacing
st.set_page_config(layout="wide", page_title="Multilingual Page")

# Create two columns — left and right halves
col1, col2 = st.columns(2)

# ---------- LEFT HALF ----------
with col1:
    st.subheader("🗣 Multilingual Paragraphs")
    
    paragraph_en = """This is a sample paragraph in English. 
    It represents the same content translated into different languages."""
    
    paragraph_si = """මෙය ඉංග්‍රීසි පාඨයේ සිංහල පරිවර්තනයකි. 
    එකම අන්තර්ගතය විවිධ භාෂාවලින් නිරූපණය කරයි."""
    
    paragraph_ta = """இது ஆங்கில பத்தி தமிழ் மொழிபெயர்ப்பு ஆகும். 
    அதே உள்ளடக்கத்தை வேறு மொழிகளில் வெளிப்படுத்துகிறது."""

    # Display paragraphs
    st.markdown(f"**English:** {paragraph_en}")
    st.markdown(f"**සිංහල:** {paragraph_si}")
    st.markdown(f"**தமிழ்:** {paragraph_ta}")

# ---------- RIGHT HALF ----------
with col2:
    st.subheader("📄 About This Section")
    st.write("This section displays some text at the top and an image below it.")

    # Display an image (replace with your own image path or URL)
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Flag_of_Sri_Lanka.svg/1024px-Flag_of_Sri_Lanka.svg.png",
        caption="Sri Lanka Flag",
        use_container_width=True
    )
