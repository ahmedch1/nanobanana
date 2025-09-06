from dotenv import load_dotenv
load_dotenv()

from google import genai
from PIL import Image
from io import BytesIO

# Configure the client with your API key
client = genai.Client()

prompt = "Restore and colorize this image from 1900"

image = Image.open("kairouan.jpg")


# Call the API to generate content
response = client.models.generate_content(
    model="models/gemini-2.5-flash-image-preview",
    contents=[prompt,image]
)

# The response can contain both text and image data.
# Iterate through the parts to find and save the image.
for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))
        image.save("kairouan-restored.png")
