import google.generativeai as genai
from google.generativeai.types import GenerationConfig
import io
import streamlit as st

genai.configure(api_key="AIzaSyB5UwPhatHQ8h0XqhFXx8BvxpONMprIXRo")


def generate_response(prompt:str, temperature:float=0.3)->str:
    try:
        system_prompt="You are a math mastermind! you are expert in algebra, geomentry, arithmetic, graphs, probability, area etc. You have to give clear and detailed answer in each steps"
        full_prompt=f"{system_prompt} Math mastermind {prompt}"
        model=genai.GenerativeModel("gemini-1.5-flash")
        response=model.generate_content(full_prompt,generation_config=GenerationConfig(temperature=temperature))
        return response.text
    except Exception as e:
        print(e)

def setup_ui():
    st.set_page_config("Math mastermind", layout="centered")
    st.title("math problem solver")
    st.write("solve problem with higher accuracy")

    with st.expander("example"):
        st.markdown("""
                    "calculus-derivative of sin60",
                    geometry-find the area of triangle (0,0,4,5)
                    algebra-x^3+5x^2+3
                    probability-deck of 3 cards
                    """)
        
        with st.form("math.form", clear_on_submit=True):
            user_input=st.text_input("enter your math problem")
            col1, col2=st.columns([3,1])
            with col1:
                submit=st.form_submit_button("solve this")
            with col2:
                difficulty=st.selectbox("level", ["basic", "intermediate", "advanced"])

    if "history" not in st.session_state:
        st.session_state.history=[]

    if submit and user_input.strip():
        prompt=f"[{difficulty} level]{user_input.strip()}"

        with st.spinner("generating response"):
            answer=generate_response(prompt)

        st.session_state.history.insert(0,{
            "question":user_input.strip(),
            "answer":answer,
            "difficulty":difficulty
        })

        st.rerun()

    elif submit:
        st.warning("please enter a math question first")

    col_clear, col_export=st.columns(2)

    with col_clear:
        if st.button("clear history"):
            st.session_state.history=[]
            st.rerun()

    with col_export:
        if st.session_state.history:
            text="\n\n".join(f"Q{idx+1}:{qa['question']}\n a{idx+1}: {qa['answer']}" for idx,qa in enumerate(st.session_state.history))
            st.download_button("download the solution", data=text, file_name="a.txt")

   

    if st.session_state.history:
        st.markdown("solution history")
        for i,qa in enumerate(st.session_state.history):
            st.markdown(f"q{i+1} ({qa['difficulty']}): {qa['question']}")
            st.markdown(f"/n answer:({qa['answer']})")

setup_ui()



    