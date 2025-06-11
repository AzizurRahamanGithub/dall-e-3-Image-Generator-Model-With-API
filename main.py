import openai
import requests

# Initialize the client with your API key
client = openai.OpenAI(api_key="")
try:
    response = client.images.generate(
        model="dall-e-3",
        prompt="Tiger is eating grass",
        n=1,
        size="1024x1024"
    )
    image_url = response.data[0].url
    print("Image URL:", image_url)

    img_data = requests.get(image_url).content
    with open('dalle_image.png', 'wb') as handler:
        handler.write(img_data)
    print("Image saved as dalle_image.png")

except Exception as e:
    print(f"OpenAI API error: {e}")
