import requests
from PIL import Image,ImageEnhance, ImageFilter
from io import BytesIO

api_key="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"

api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"

def img_g(prompt:str)->Image.Image:
  headers={"Authorization":f"Bearer {api_key}"}
  payload={"inputs": prompt}

  try:
    response=requests.post(api_url,headers=headers,json=payload,timeout=30)
    response.raise_for_status()

    if "image" in response.headers.get("content-type",''):
      img=Image.open(BytesIO(response.content))
      return img

    else:
      raise Exception("the output is not valid, image couldnt be generated")
  except Exception as e:
    raise Exception(f"the exception is {e}")


def p(img:Image.Image)->Image.Image:
  enhancer=ImageEnhance.Brightness(img)
  bright=enhancer.enhance(0.8)
  enhancer=ImageEnhance.Contrast(bright)
  contrast=enhancer.enhance(1.7)

  s=contrast.filter(ImageFilter.GaussianBlur(radius=7))
  return s

def main():
  print("welcome to this program")
  print("type q to exit this program")

  while True:
    u=input("enter the prompt for the image that you would like to generate")
    if u.lower()=="q":
      print("goodbye")
      break

    else:
      try:
        img1=img_g(u)
        img_enhance=p(img1)

        img_enhance.show()

      except Exception as E:
        print(f"an error has occured{E}")

main()

