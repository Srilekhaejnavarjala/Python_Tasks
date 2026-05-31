# ============================================================
# 🚀 Gemini AI Streamlit Frontend
# ============================================================

# Install:
# pip install streamlit requests

import streamlit as st
import requests

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Gemini AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# FASTAPI URLS
# ============================================================

ASK_URL = "http://127.0.0.1:8000/ask"
SUMMARY_URL = "http://127.0.0.1:8000/summarize"

# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* ============================================================
MAIN BACKGROUND
============================================================ */

.stApp{
    background-color: #0f0f0f;
    color: #e7dfd6;
}

/* ============================================================
SIDEBAR
============================================================ */

section[data-testid="stSidebar"]{
    background-color: #161616;
    border-right: 1px solid #2a2a2a;
}

/* Sidebar Radio Buttons */

div[role="radiogroup"] label {
    background-color: #1f1f1f;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
    border: 1px solid #2d2d2d;
    transition: 0.3s ease;
}

div[role="radiogroup"] label:hover {
    background-color: #2a2a2a;
    border: 1px solid #c6ac8f;
}

/* ============================================================
TITLE
============================================================ */

.main-title{
    text-align:center;
    font-size:52px;
    font-weight:700;
    color:#f1e9dc;
    margin-bottom:8px;
    letter-spacing:1px;
}

.sub-title{
    text-align:center;
    color:#b8b0a7;
    font-size:18px;
    margin-bottom:35px;
}

/* ============================================================
CHAT BOXES
============================================================ */

.user-msg{
    background-color:#c6ac8f;
    color:#111111;
    padding:18px;
    border-radius:20px 20px 0px 20px;
    margin:12px 0;
    width:fit-content;
    max-width:75%;
    margin-left:auto;
    font-size:16px;
    font-weight:500;
}

.bot-msg{
    background-color:#1c1c1c;
    border:1px solid #2b2b2b;
    padding:18px;
    border-radius:20px 20px 20px 0px;
    margin:12px 0;
    width:fit-content;
    max-width:75%;
    color:#ece3d6;
    font-size:16px;
}

/* ============================================================
SUMMARY BOX
============================================================ */

.summary-box{
    background-color:#1b1b1b;
    border:1px solid #2c2c2c;
    padding:30px;
    border-radius:24px;
    margin-top:25px;
}

.summary-title{
    font-size:28px;
    font-weight:600;
    margin-bottom:15px;
    color:#d6bfa7;
}

/* ============================================================
TEXT AREA
============================================================ */

textarea{
    background-color:#1a1a1a !important;
    color:#ece3d6 !important;
    border-radius:18px !important;
    border:1px solid #333333 !important;
    padding:15px !important;
}

/* ============================================================
BUTTONS
============================================================ */

.stButton > button{
    width:100%;
    height:55px;
    border:none;
    border-radius:16px;
    background-color:#c6ac8f;
    color:#111111;
    font-size:18px;
    font-weight:600;
    transition:0.3s ease;
}

.stButton > button:hover{
    background-color:#d8c3ab;
    transform:translateY(-2px);
}

/* ============================================================
CHAT INPUT
============================================================ */

.stChatInput{
    background-color:#1a1a1a;
}

/* ============================================================
FEATURE CARD
============================================================ */

.feature-card{
    background-color:#1b1b1b;
    border:1px solid #2a2a2a;
    border-radius:20px;
    padding:20px;
    margin-top:15px;
}

.feature-title{
    font-size:20px;
    font-weight:600;
    color:#d9c2a7;
}

.feature-text{
    color:#c7beb5;
    margin-top:10px;
    line-height:1.8;
}

/* ============================================================
SCROLLBAR
============================================================ */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #111111;
}

::-webkit-scrollbar-thumb {
    background: #3a3a3a;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #555555;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    """
    <h1 style='text-align:center; color:#f1e9dc;'>
        🤖 Gemini AI
    </h1>
    """,
    unsafe_allow_html=True
)

page = st.sidebar.radio(
    "Choose Feature",
    [
        "💬 AI Chat",
        "📝 Text Summarizer"
    ]
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    <div class="feature-card">

        <div class="feature-title">
            ✨ Features
        </div>

        <div class="feature-text">
            ✅ AI Chatbot <br>
            ✅ AI Text Summarizer <br>
            ✅ FastAPI Backend <br>
            ✅ Gemini AI Integration <br>
            ✅ Modern Aesthetic UI
        </div>

    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# AI CHAT PAGE
# ============================================================

if page == "💬 AI Chat":

    st.markdown(
        '<div class="main-title">Gemini AI Assistant</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">Smart conversational AI powered by Gemini</div>',
        unsafe_allow_html=True
    )

    # ========================================================
    # DISPLAY CHAT MESSAGES
    # ========================================================

    for chat in st.session_state.messages:

        if chat["role"] == "user":

            st.markdown(
                f"""
                <div style="display:flex; justify-content:flex-end;">
                    <div class="user-msg">
                        👤 {chat['content']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div style="display:flex; justify-content:flex-start;">
                    <div class="bot-msg">
                        🤖 {chat['content']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # ========================================================
    # CHAT INPUT
    # ========================================================

    question = st.chat_input(
        "Ask anything..."
    )

    if question:

        # Add User Message
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.spinner("Gemini is thinking..."):

            try:

                response = requests.post(
                    ASK_URL,
                    json={
                        "question": question
                    }
                )

                data = response.json()

                answer = data.get(
                    "answer",
                    "No response generated."
                )

            except Exception as e:

                answer = str(e)

        # Add Bot Response
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        st.rerun()

# ============================================================
# TEXT SUMMARIZER PAGE
# ============================================================

elif page == "📝 Text Summarizer":

    st.markdown(
        '<div class="main-title">AI Text Summarizer</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">Paste articles and get concise AI summaries instantly</div>',
        unsafe_allow_html=True
    )

    article = st.text_area(
        "Paste Article / Research Paper / Notes",
        height=320,
        placeholder="Paste long article here..."
    )

    summarize_button = st.button(
        "✨ Generate Summary"
    )

    if summarize_button:

        if article.strip() == "":

            st.warning("Please enter some text.")

        else:

            with st.spinner("Analyzing article with Gemini AI..."):

                try:

                    response = requests.post(
                        SUMMARY_URL,
                        json={
                            "text": article
                        }
                    )

                    data = response.json()

                    summary = data.get(
                        "summary",
                        "No summary generated."
                    )

                except Exception as e:

                    summary = str(e)

            st.markdown(
                f"""
                <div class="summary-box">

                    <div class="summary-title">
                        📄 AI Generated Summary
                    </div>

                    <hr style="border:1px solid #333333;">

                    <p style="font-size:17px; line-height:1.9;">
                        {summary}
                    </p>

                </div>
                """,
                unsafe_allow_html=True
            )