import base64
import google.generativeai as genai
import os
import json

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def decode_image_from_base64(image_base64: str):
    return base64.b64decode(image_base64)

def call_gemini_vision_api(image_data: bytes, user_prompt: str):
    model = genai.GenerativeModel('gemini-pro-vision')
    image_parts = [
        {
            "mime_type": "image/jpeg",  # Assuming JPEG, adjust if other formats are expected
            "data": image_data
        }
    ]
    prompt_parts = [
        user_prompt,
        image_parts[0]
    ]
    
    response = model.generate_content(prompt_parts)
    
    # Attempt to parse the response as JSON. Gemini might return text that needs parsing.
    try:
        # Assuming the response.text is a JSON string
        return json.loads(response.text)
    except json.JSONDecodeError:
        print(f"Warning: Gemini API response was not a direct JSON. Attempting to clean and parse. Response: {response.text}")
        # Sometimes Gemini returns markdown code block, try to extract JSON from it
        if '```json' in response.text and '```' in response.text:
            json_str = response.text.split('```json')[1].split('```')[0]
            return json.loads(json_str)
        return {"error": "Failed to parse Gemini API response", "raw_response": response.text}



