import streamlit as st
import google.generativeai as genai
import datetime, os

genai.configure(api_key="AIzaSyB5UwPhatHQ8h0XqhFXx8BvxpONMprIXRo")

if "model_name" not in st.session_state:
    st.session_state.model_name="gemini-1.5-flash"

if "history" not in st.session_state:
    st.session_state.history=[]



def generate_response(prompt,temp=0.7):
    try:
        model=genai.GenerativeModel(st.session_state.model_name)
        return model.generate_content(prompt,generation_config={"temperature":temp}).text
        
    except Exception as e:
        return f"error:{e}"
    
def setup():
    st.title("talking AI")
    st.session_state.model=st.selectbox("Model", ["gemini-1.5-flash", "gemini-1.5-pro"])
    temp=st.slider("Creativity", 0.0,1.0,0.7)

    q=st.text_input("Ask ")
    if q:
        st.session_state.history+=[("You",q),("AI", generate_response(q,temp))]
    
    for s,m in st.session_state.history:
        bg,align=("#DCF8C6", "right") if s=="You" else ("#EAEAEA", "left")
        st.markdown(f"<div style='background:{bg}; padding:5px; border-radius:8px; margin:3px; max-wdith:70%; float:{align}; clear:both'><b>{s}:</b>{m}</div>", unsafe_allow_html=True)

    if st.session_state.history:
        st.download_button("download".join([f"{s}:{t}" for s,t in st.session_state.history]),f"chat_{datetime.datetime.now().strftime('%H%M%S')}.txt" )
    if st.button("clear chat"):st.session_state.history=[]; st.rerun()

setup()
    




