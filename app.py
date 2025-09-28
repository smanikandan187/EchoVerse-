import streamlit as st
from src.tone_rewrite import rewrite_text
from src.tts import synthesize

st.set_page_config(page_title="EchoVerse", layout="wide")

st.title("EchoVerse – AI-Powered Audiobook Creation Tool (Open Source)")

tone_option = st.selectbox(
    "Select Tone",
    ["Neutral", "Suspenseful", "Inspiring"]
)

st.header("Input Text")
uploaded_file = st.file_uploader("Upload a .txt file", type=".txt")

if uploaded_file:
    raw_text = uploaded_file.read().decode("utf-8")
else:
    raw_text = st.text_area("Paste or type your text here...")

if raw_text:
    st.subheader("Original Text")
    st.write(raw_text)
    if st.button("Rewrite Text"):
        rewritten = rewrite_text(raw_text, tone_option)
        st.subheader("Tone-Adapted Text")
        st.write(rewritten)

        st.subheader("Side-by-Side Comparison")
        col1, col2 = st.columns(2)
        col1.write("Original Text")
        col1.write(raw_text)
        col2.write("Adapted Text")
        col2.write(rewritten)

        if st.button("Generate Audio"):
            audio_file_path = synthesize(rewritten)
            audio_bytes = open(audio_file_path, 'rb').read()
            st.audio(audio_bytes, format='audio/wav')
            st.download_button(
                label="Download Audio",
                data=audio_bytes,
                file_name="audiobook.wav",
                mime="audio/wav"
            )
