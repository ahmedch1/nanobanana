from dotenv import load_dotenv
load_dotenv()

from google import genai
from PIL import Image
from io import BytesIO

# Configure the client with your API key
client = genai.Client()

prompt = """Using the image of the cat, create a photorealistic,
street-level view of the cat walking along a sidewalk in a
New York City neighborhood, with the blurred legs of pedestrians
and yellow cabs passing by in the background."""

image=Image.open("cat.png")

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
        image.save("cat2.png")
