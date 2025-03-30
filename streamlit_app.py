import streamlit as st

st.set_page_config(page_title="🪞 The Mirror Room", layout="centered")

st.markdown("<h1 style='text-align: center;'>🪞 The Mirror Room</h1>", unsafe_allow_html=True)

st.write("This space was created for those who carry an invisible weight — the kind that doesn't respond to 'just push through it' advice. You're not here to close deals. You're here to align with people.")

user_input = st.text_area("What are you sitting with right now?", placeholder="Drop your truth here. No rules.")

if user_input:
    st.markdown("---")
    st.subheader("Reflection from your highest self:")
    st.write(f"“Even now — with all that doubt — you’re still showing up. That’s not failure. That’s sacred.”")
import cv2
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

class MirrorTransformer(VideoTransformerBase):
    def transform(self, frame):
        return cv2.flip(frame.to_ndarray(format="bgr24"), 1)  # Mirror horizontally

st.markdown("---")
st.subheader("🪞 See yourself:")

webrtc_streamer(key="mirror", video_transformer_factory=MirrorTransformer)
