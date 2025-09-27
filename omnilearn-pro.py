# OmniLearn+ - All-in-One Prototype
# Created by Akin Sokpah
# WARNING: This is a DEMO. Not production-ready.

import streamlit as st
import requests
import json
import os
from datetime import datetime

# ======================
# CONFIGURATION (ADD YOUR KEYS HERE LATER)
# ======================
# NEVER commit real keys to GitHub!
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "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")  # Get from https://platform.openai.com
# For real video: Use Cloudflare Stream, AWS IVS, or Mux (add keys in env vars)

# ======================
# MOCK DATA (Replace with real DB later)
# ======================
mock_courses = [
    {"id": 1, "title": "AI for Beginners", "instructor": "Akin Sokpah", "duration": "2h"},
    {"id": 2, "title": "Build TikTok Clone", "instructor": "Dev Master", "duration": "4h"},
]

mock_videos = [
    {"id": 1, "title": "How to learn fast!", "creator": "Akin", "views": "1.2K"},
    {"id": 2, "title": "Python in 60 sec", "creator": "CodeGuru", "views": "5.4K"},
]

# ======================
# AI HELPER FUNCTION
# ======================
def ask_ai(question):
    if "YOUR_OPENAI_KEY_HERE" in OPENAI_API_KEY:
        return "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"
    
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
            json={
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": f"Explain like I'm 15: {question}"}],
                "max_tokens": 150
            }
        )
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"AI Error: {str(e)}"

# ======================
# STREAMLIT UI
# ======================
st.set_page_config(page_title="OmniLearn+ by Akin Sokpah", layout="wide")
st.title("🌟 OmniLearn+")
st.markdown("### *All-in-One Learning, Creation & Entertainment*")
st.caption("Created by **Akin Sokpah**")

# Navigation
tabs = st.tabs(["🏠 Home", "🎓 Courses", "🎬 Short Videos", "🤖 AI Tutor", "🌐 Website Builder"])

# --- HOME TAB ---
with tabs[0]:
    st.header("Welcome to OmniLearn+!")
    st.write("Your unified platform for learning, creating, and connecting.")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📚 Learn")
        st.write("Take courses from experts worldwide.")
    with col2:
        st.subheader("🎥 Create & Share")
        st.write("Upload videos, go live, and build your audience.")

# --- COURSES TAB ---
with tabs[1]:
    st.header("Online Courses")
    for course in mock_courses:
        with st.expander(f"{course['title']} - {course['duration']}"):
            st.write(f"**Instructor**: {course['instructor']}")
            st.button("Enroll", key=f"enroll_{course['id']}")

# --- SHORT VIDEOS TAB ---
with tabs[2]:
    st.header("Short Videos (TikTok Style)")
    for vid in mock_videos:
        st.video("https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4")  # Demo video
        st.subheader(vid["title"])
        st.caption(f"By {vid['creator']} • {vid['views']} views")
        st.divider()

# --- AI TUTOR TAB ---
with tabs[3]:
    st.header("AI Learning Assistant")
    user_question = st.text_input("Ask anything about your courses:", placeholder="e.g., What is machine learning?")
    if user_question:
        with st.spinner("Thinking..."):
            ai_response = ask_ai(user_question)
        st.success("AI Response:")
        st.write(ai_response)

# --- WEBSITE BUILDER TAB ---
with tabs[4]:
    st.header("Drag & Drop Website Builder (Demo)")
    st.info("In a real app, this would be a visual editor like Wix.")
    site_title = st.text_input("Website Title", "My OmniLearn+ Site")
    site_content = st.text_area("Page Content", "Welcome to my course!")
    if st.button("Preview Website"):
        st.subheader(site_title)
        st.write(site_content)
        st.code(f"<h1>{site_title}</h1><p>{site_content}</p>", language="html")

# --- FOOTER ---
st.markdown("---")
st.caption("© 2024 OmniLearn+ by Akin Sokpah. This is a prototype. Not for production use.")
