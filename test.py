import requests

API_KEY = ""
prompt = "Tiger is flying on the sky"
api_url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-3.0-generate-002:predict?key={API_KEY}"

payload = {
    "instances": [
        {
            "prompt": {
                "text": prompt
            }
        }
    ]
}

response = requests.post(api_url, json=payload)

if response.status_code != 200:
    print("Error:", response.status_code)
    print(response.text)
else:
    print(response.json())

