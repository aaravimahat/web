import streamlit as st
import google.generativeai as genai
from google.generativeai.types import GenerationConfig
from io import BytesIO
from PIL import Image
import time,re
import requests

genai.configure(api_key="AIzaSyB5UwPhatHQ8h0XqhFXx8BvxpONMprIXRo")

hf_api_key="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"
hf_api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
hf_headers={"Authorization": f"Bearer {hf_api_key}"}

def generate_gemini_response(prompt, temperature=0.4):
    try:
        model=genai.GenerativeModel("gemini-1.5-flash")
        response=model.generate_content(prompt,generation_config={"temperature":temperature})
        return response.text
    except Exception as e:
        print(f"exception found {e}")


def generate_math_response(prompt:str, difficulty:str,temperature:float=0.3)->str:
    try:
        system_prompt="you are a math mastermind! you are expert in arithmetics, geometry, alegbra"
        full_prompt=f"{system_prompt}\n math problem solver {prompt}"
        model=genai.GenerativeModel("gemini-1.5-flash")
        response=model.generate_content(full_prompt,generation_config=GenerationConfig(temperature=temperature))
        return generate_gemini_response(full_prompt)
    except Exception as e:
        return e
    
def is_safe_prompt(prompt:str)->bool:
    forbidden_keywords=["violence", "terror", "attack", "suicide", "bomb", "abuse", "murder", "self-harm", "hate speech", "nudity", "racism"]
    pattern=re.compile("|".join(forbidden_keywords),re.IGNORECASE)
    return not bool(pattern.search(prompt))

def generate_image(prompt:str)->Image.Image:
    if not is_safe_prompt(prompt):
        return None,"prompt contains restricted content"
    try:
        payload={"inputs":prompt}
        response=requests.post(hf_api_url, headers=hf_headers, json=payload, timeout=30)

        if response.status_code==200:
            image=Image.open(BytesIO(response.content))
            return image, "image is generated with stable diffusor"
        
        else:
            return None, f"error:{response.text}"
        
    except Exception as e:
        return None, f"exception {str(e)}"
    
st.set_page_config("AI app", layout="centered")
st.title("SMART AI")

tab1,tab2,tab3=st.tabs(["math solver", "AI general assistant","AI image generatorst"])

with tab1:
    st.header("math problem solver")
    with st.expander("example breakdown"):
        st.markdown("""
                "calculus-derivative of sin60",
                geometry-find area of triangle(0,4,5,6)
                algebra-x^2+5x+3
                probability-deck of 5 cards
                """)
        
    with st.form("math form", clear_on_submit= True):
        user_input=st.text_area("enter your math problem",height=150)
        difficulty=st.selectbox("difficulty level",['basic', 'intermediate', 'advance'])
        submit=st.form_submit_button("solve")

    if submit and user_input.strip():
        with st.spinner("solving"):
            answer=generate_math_response(user_input.strip(),difficulty)
            st.success("solution generated")
            st.markdown(answer)

    elif submit:
        st.warning('please enter a math problem first')

with tab2:
    st.header("ask me anything")
    user_input=st.text_input("enter your questions realted to any topic")
    if st.button("get answer"):
        if user_input.strip():
            with st.spinner("loading answer"):
                answer=generate_gemini_response(user_input)
                st.success("answer generated")
                st.markdown(answer)
        else:
            st.warning("please enter the question first")

with tab3:
    st.header("AI IMAGE GENERATOR")
    img_prompt=st.text_area("enter a creative description for image generation")

    if st.button("generate image"):
        if img_prompt.strip():
            with st.spinner("creating image"):
                image,msg=generate_image(img_prompt.strip())
                st.info(msg)

                if image:
                    st.image(image,caption="generated with stable diffusion", use_column_width=True)
                    if st.button("save"):
                        image.save("a.png")
                        st.success("image saved as a.png")
        else:
            st.warning("please enter a valid prompt")


    

                                
        

    



    

