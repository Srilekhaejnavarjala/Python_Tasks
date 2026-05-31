# ============================================================
# Streamlit Frontend
# ============================================================

import streamlit as st
from main import generate_answer

# ============================================================
# Page Config
# ============================================================

st.set_page_config(
    page_title="AI Learning Assistant",
    page_icon="🤖",
    layout="wide"
)

# ============================================================
# Header
# ============================================================

st.title("🤖 AI Learning Assistant")

st.markdown("""
Ask questions related to:

✅ Python  
✅ FastAPI  
✅ Flask  
✅ Machine Learning  
✅ Deep Learning  
✅ Data Science  
""")

# ============================================================
# User Input
# ============================================================

question = st.text_area(
    "Enter your question",
    height=150
)

# ============================================================
# Generate Button
# ============================================================

if st.button("Generate Answer"):

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner("Generating response..."):

            try:

                answer = generate_answer(question)

                st.success("Response Generated")

                st.markdown("### Answer")

                st.write(answer)

            except Exception as e:

                st.error(f"Error: {str(e)}")