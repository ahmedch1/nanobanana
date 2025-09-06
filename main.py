from dotenv import load_dotenv
load_dotenv()

from google import genai
from PIL import Image
from io import BytesIO

# Configure the client with your API key
client = genai.Client()

# Create a chat
chat = client.chats.create(
    model="gemini-2.5-flash-image-preview"
)

# Send the first message with the image and prompt
response1 = chat.send_message(
    [
        "Change the cat to a siamese cat, leave everything else the same",
        Image.open("cat.png"),
    ]
)

# Save the first image of the bengal cat
for part in response1.candidates[0].content.parts:
    if hasattr(part, "inline_data") and part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))
        image.save("siamese_cat.png")
        break  # Save only the first image

# Send the second message to further modify the image
response2 = chat.send_message("The cat should wear a funny party hat")

# Save the second image of the bengal cat with a funny party hat
for part in response2.candidates[0].content.parts:
    if hasattr(part, "inline_data") and part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))
        image.save("siamese_funny_cat.png")
        break  # Save only the first image
    elif hasattr(part, "text") and part.text is not None:
        print(part.text)
