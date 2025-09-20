import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyB5UwPhatHQ8h0XqhFXx8BvxpONMprIXRo")

model=genai.GenerativeModel("gemini-2.5-flash")

def generate_response(prompt):
    try:
        response=model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        print(e)


st.set_page_config(page_title="welcome to the AI assistant", layout="centered")
st.title("AI assistant")
st.write("ask me anything")


if "history" not in st.session_state:
    st.session_state.history=[]

if st.button("clear chat"):
    st.session_state.history=[]
    st.rerun()


user_input=st.text_input("ask any question")

if st.button("ask"):
    if user_input.strip():
        with st.spinner("generating respone"):
            answer=generate_response(user_input.strip())
            st.session_state.history.append({"question":user_input.strip(), "answer":answer})
    else:
        st.warning("please enter a question first")


st.markdown("""
<style>
            .history{
            max-height:300px;
            overflow-y:auto;
            border:7px solid black;
            padding:11px;
            background-color:black;
            font-family:Arial, sans-serif;
            }

            .question{
            font-weight:bold;
            color:white;
            margin:13px;
            }

            .answer{
            color:white;
            margin:16px;
            white-space: pre-wrap;}

""", unsafe_allow_html=True)

history_html="<div class='history'>"
for i,q in enumerate(st.session_state.history,1):
    qa=q["question"]
    a=q["answer"]
    history_html+=f"<div class='question'> Q{i}:{qa}<br></div>"
    history_html+=f"<div class='question'> Q{i}:{a}<br></div>"

history_html+="</div>"

st.markdown(history_html, unsafe_allow_html=True)


