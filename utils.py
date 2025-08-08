import google.generativeai as genai
import os
import json
from PIL import Image
import io

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def call_gemini_vision_api(image_data: bytes, content_type: str):
    """
    Chama a API do Gemini para análise de imagens com prompt otimizado
    """
    
    # Criar um objeto Image do PIL a partir dos bytes
    image = Image.open(io.BytesIO(image_data))
    
    # Usar o modelo Gemini mais atual
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Prompt baseado no original do usuário, mas adaptado e funcional
    prompt = """
    You are a professional nutrition analyst. Your goal is to analyze this food photo for each visible item and output a structured JSON with clear calorie and macro estimates.

    CORE FUNCTIONALITY:
    • When shown a food image, identify each item and its main components (protein, carb, fat, etc.)
    • Assume a standard reference (e.g. 26 cm dinner plate, 250 ml cup, standard fork) for scale  
    • Note if it looks like a restaurant-prepared dish—if so, assume extra cooking fat: sauté or sauce fat up by ~1 Tbsp (14 g) per portion
    • Estimate portion sizes in grams. Use reference cues in the image (cups, standard glass size, bread size, common utensils) to scale portions
    • Make assumptions realistic. Prefer common serving sizes
    • List any assumptions (shape, density, coverage %) you use to estimate size   
    • Estimate calories & macros per item using trusted databases (USDA FoodData Central, European equivalents), adjusting for added restaurant fat
    • Note visible cooking methods or add-ins (oil, sauce, butter)
    • Calculate calories for each item, giving a plausible range
    • Sum to a total calories range

    JSON OUTPUT SCHEMA (return ONLY this JSON, no additional text):
    {
      "overview": "Brief sentence about the full plate or spread",
      "short_name": "burger with fries",
      "items": [
        {
          "name": "Item name",
          "type": "protein | carb | fat | vegetable | fruit | beverage",
          "portion_size": "e.g. 1 cup, 2 slices",
          "cooking_method": "if obvious",
          "macros_g": {
            "protein": 0.0,
            "carbs": 0.0,
            "fat": 0.0
          },
          "calories_kcal": {
            "low": 0,
            "high": 0
          },
          "assumptions": "Any guesses you made"
        }
      ],
      "total_calories_kcal": {
        "low": 0,
        "high": 0
      },
      "total_macros": {
        "proteins": {
          "low": 0.0,
          "high": 0.0
        },
        "carbs": {
          "low": 0.0,
          "high": 0.0
        },
        "fat": {
          "low": 0.0,
          "high": 0.0
        }
      },
      "notes": "Any limitations or estimate may vary warnings"
    }

    FOOD ANALYSIS GUIDELINES:
    • Start with "overview" for the whole meal
    • For each item, fill every field in the schema
    • Give calories as a low–high range
    • Explain assumptions in the "assumptions" field
    • If unsure or image is unclear, add warnings in "notes"
    • Use realistic portion estimates based on visual cues
    • Account for cooking methods that add calories (frying, sauces, etc.)
    
    Return ONLY the JSON response, no additional text or formatting.
    """
    
    try:
        response = model.generate_content([prompt, image])
        
        # Tentar fazer parse do JSON da resposta
        response_text = response.text.strip()
        
        # Remover markdown se presente
        if response_text.startswith('```json'):
            response_text = response_text.split('```json')[1].split('```')[0]
        elif response_text.startswith('```'):
            response_text = response_text.split('```')[1].split('```')[0]
        
        # Parse do JSON
        return json.loads(response_text)
        
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        print(f"Response text: {response.text}")
        
        # Fallback response se não conseguir fazer parse
        return {
            "overview": "Análise não pôde ser completada",
            "short_name": "Erro na análise",
            "items": [{
                "name": "Item não identificado",
                "type": "unknown",
                "portion_size": "Não determinado",
                "cooking_method": None,
                "macros_g": {"protein": 0, "carbs": 0, "fat": 0},
                "calories_kcal": {"low": 0, "high": 0},
                "assumptions": "Erro na análise da imagem"
            }],
            "total_calories_kcal": {"low": 0, "high": 0},
            "total_macros": {
                "proteins": {"low": 0, "high": 0},
                "carbs": {"low": 0, "high": 0},
                "fat": {"low": 0, "high": 0}
            },
            "notes": f"Erro ao processar a análise: {str(e)}"
        }
    
    except Exception as e:
        print(f"General error: {e}")
        raise Exception(f"Erro na API do Gemini: {str(e)}")



