import requests
from PIL import Image
from io import BytesIO

api_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IjE0ZWZhNTcwYTAwOTFjODQ4ODZjYjQ2YmY0ZWQwZGUwIiwiY3JlYXRlZF9hdCI6IjIwMjUtMDctMTlUMDQ6Mzc6MTcuNzE2MDQyIn0.ngY8S7nQ03_SJDwN7yVCd-x_mDZShvlqjkezjT7vcck"



a = input("Enter a description for the image: ")
url = "https://api.monsterapi.ai/v1/generate/txt2img"
headers = {"Authorization": f"Bearer {api_token}"}
response = requests.post(url, json={"prompt": a, "safe_filter": True}, headers=headers)

if response.status_code == 200:
    print("Generating...")
    process_id = response.json().get("process_id")

    while True:
        status_data = requests.get(f"https://api.monsterapi.ai/v1/status/{process_id}", headers=headers).json()
        status = status_data.get("status")
        # print(status_data)

        if status == "COMPLETED":
            image_url = status_data['result']['output'][0]
            img = Image.open(BytesIO(requests.get(image_url).content))
            img.show()
            print()
            break
        elif status == "FAILED":
            print("Image generation failed.")
            break
else:
    print(f"Error: {response.status_code}")

