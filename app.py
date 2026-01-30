import streamlit as st
from generator import generate_email
from validator import validate_email

st.set_page_config(page_title="Structured Content Generator")
st.title("Structured Email Generator")

purpose = st.text_input("Email purpose")
key_points = st.text_area("Key points")
tone = st.selectbox("Tone", ["formal", "friendly", "confident"])

if st.button("Generate Email"):
    if not purpose.strip() or not key_points.strip():
        st.warning("Please fill in all fields.")
    else:
        with st.spinner("Generating structured email..."):
            try:
                email = generate_email(tone, purpose, key_points)
                validate_email(email)
                st.subheader("Generated Email (Structured JSON)")
                st.json(email)
            except Exception as e:
                st.error("Failed to generate a valid structured email.")
                st.caption(str(e))
