import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import re

api_token="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"

def prompt_safe(prompt:str)->bool:
    forbidden_keywords=["violence", "terror", "attack", "suicide", "bomb", "abuse", "murder", "self-harm", "hate speech", "nudity", "racism"]
    pattern=re.compile("|".join(forbidden_keywords),re.IGNORECASE)
    return not bool (pattern.search(prompt))

def generate_image(prompt:str):
    if not prompt_safe(prompt):
        return None, "prompt contains restricted content"
    
    try:
        api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
        headers={"Authorization":f"Bearer {api_token}"}
        payload={"inputs":prompt}

        response=requests.post(api_url,headers=headers, json=payload)
        if response.status_code==200:
            image=Image.open(BytesIO(response.content))
            return image, "image is generated with stable diffusor"
        
        else:
            return None, f"error:{response.text}"
        
    except Exception as e:
        return None, f"exception {str(e)}"
    
st.set_page_config(page_title="AI image generator", layout="wide")
st.title("AI image generator")
st.write("generate images using stable diffusor (hugging api)")

prompt=st.text_area("enter your image description",placeholder="eg. a futuristic city")

if st.button("generate with stable diffusor"):
    with st.spinner("generating..."):
        image,msg=generate_image(prompt)
        st.info(msg)

        if image:
            st.image(image,caption="generated using stable diffusor", use_column_width=True)
            if st.button("save image"):
                image.save("a.png")
                st.success("image saved as a.png")
                
    

