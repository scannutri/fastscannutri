import os
from dotenv import load_dotenv
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import logging

# Imports para Vertex AI
import vertexai
from vertexai.generative_models import GenerativeModel, Part

load_dotenv()

# Configuração do Vertex AI
PROJECT_ID = os.getenv("VERTEX_AI_PROJECT_ID", "your-project-id")
LOCATION = os.getenv("VERTEX_AI_LOCATION", "us-central1")
vertexai.init(project=PROJECT_ID, location=LOCATION)

app = FastAPI(
    title="FastScanNutri API",
    description="API de Análise Nutricional com IA",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)

from model import GeminiVisionResponse
from db import create_table_if_not_exists, insert_analysis_result

@app.on_event("startup")
async def startup_event():
    await create_table_if_not_exists()

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastScanNutri API! 🍎", "docs": "/docs"}

@app.get("/health")
async def health_check():
    """Endpoint para verificar a saúde da API"""
    import time
    
    health_status = {
        "status": "healthy",
        "timestamp": int(time.time()),
        "version": "1.0.0",
        "services": {
            "api": "running",
            "database": "unknown",
            "vertex_ai": "unknown"
        }
    }
    
    # Verificar conexão com database
    try:
        if os.getenv("DATABASE_URL"):
            health_status["services"]["database"] = "configured"
        else:
            health_status["services"]["database"] = "not_configured"
    except Exception as e:
        health_status["services"]["database"] = "error"
        logging.warning(f"Database health check failed: {e}")
    
    # Verificar Vertex AI
    try:
        if os.getenv("VERTEX_AI_PROJECT_ID") and os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
            health_status["services"]["vertex_ai"] = "configured"
        else:
            health_status["services"]["vertex_ai"] = "not_configured"
            health_status["status"] = "degraded"
    except Exception as e:
        health_status["services"]["vertex_ai"] = "error"
        health_status["status"] = "degraded"
    
    return health_status

@app.post("/analyze", response_model=GeminiVisionResponse)
async def analyze_image(
    image: UploadFile = File(..., description="Imagem do alimento para análise"),
    user_id: str = Form(..., description="ID único do usuário"),
    nome: str = Form(None, description="Nome do alimento (opcional)")
):
    """
    Analisa uma imagem de alimento e retorna informações nutricionais detalhadas usando Vertex AI.
    
    - **image**: Arquivo de imagem (JPG, PNG, etc.)
    - **user_id**: ID único do usuário
    - **nome**: Nome do alimento (opcional)
    """
    logging.info(f"Received analysis request for user: {user_id}")
    
    # Verificar se é uma imagem
    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Arquivo deve ser uma imagem")
    
    try:
        # Ler os dados da imagem
        image_data = await image.read()
        logging.info(f"Image loaded successfully, size: {len(image_data)} bytes")
        
        # Criar o objeto Part para a imagem
        image_part = Part.from_data(data=image_data, mime_type=image.content_type)
        
        # Prompt para análise nutricional detalhada no formato correto
        prompt_nutricional = """
        Analise esta imagem de alimento e forneça informações nutricionais detalhadas no seguinte formato JSON exato:
        
        {
            "overview": "Descrição geral do prato/alimento",
            "short_name": "Nome curto do prato",
            "items": [
                {
                    "name": "Nome do ingrediente",
                    "type": "carb/protein/fat/veggie",
                    "portion_size": "quantidade estimada",
                    "cooking_method": "método de cozimento (opcional)",
                    "macros_g": {
                        "protein": 0.0,
                        "carbs": 0.0,
                        "fat": 0.0
                    },
                    "calories_kcal": {
                        "low": 0.0,
                        "high": 0.0
                    },
                    "assumptions": "suposições sobre o ingrediente"
                }
            ],
            "total_calories_kcal": {
                "low": 0.0,
                "high": 0.0
            },
            "total_macros": {
                "proteins": {"low": 0.0, "high": 0.0},
                "carbs": {"low": 0.0, "high": 0.0},
                "fat": {"low": 0.0, "high": 0.0}
            },
            "notes": "Observações e recomendações nutricionais"
        }
        
        Forneça valores aproximados realistas baseados no que você vê na imagem.
        Responda APENAS com o JSON válido, sem texto adicional.
        """
        
        # Criar a lista de partes para a requisição
        parts_for_gemini = [image_part, prompt_nutricional]
        
        # Carregar o modelo Vertex AI
        model = GenerativeModel("gemini-2.0-flash-001")
        
        # Fazer a chamada para a API Vertex AI
        response = model.generate_content(parts_for_gemini)
        logging.info("Vertex AI called successfully.")
        
        # Tentar parsear a resposta JSON
        try:
            import json
            # Extrair JSON da resposta
            response_text = response.text.strip()
            if response_text.startswith('```json'):
                response_text = response_text.replace('```json', '').replace('```', '').strip()
            
            gemini_response_data = json.loads(response_text)
        except json.JSONDecodeError:
            # Se falhar no parse JSON, criar uma resposta padrão com o formato correto
            gemini_response_data = {
                "overview": "Análise não pôde ser completada automaticamente",
                "short_name": "Alimento",
                "items": [
                    {
                        "name": "Alimento não identificado",
                        "type": "veggie",
                        "portion_size": "porção média",
                        "cooking_method": "não especificado",
                        "macros_g": {
                            "protein": 5.0,
                            "carbs": 20.0,
                            "fat": 3.0
                        },
                        "calories_kcal": {
                            "low": 120.0,
                            "high": 150.0
                        },
                        "assumptions": "Estimativa baseada em alimentos similares"
                    }
                ],
                "total_calories_kcal": {
                    "low": 120.0,
                    "high": 150.0
                },
                "total_macros": {
                    "proteins": {"low": 5.0, "high": 5.0},
                    "carbs": {"low": 20.0, "high": 20.0},
                    "fat": {"low": 3.0, "high": 3.0}
                },
                "notes": "Consulte um nutricionista para análise detalhada. Resposta original: " + response.text[:200] + "..."
            }
        
        # Validar e converter a resposta para o modelo Pydantic
        analysis_result = GeminiVisionResponse(**gemini_response_data)
        logging.info("Vertex AI response parsed and validated.")
        
        # Salvar no banco de dados (se configurado)
        if os.getenv("DATABASE_URL"):
            try:
                await insert_analysis_result(user_id, nome, analysis_result.dict())
                logging.info("Analysis result saved to database.")
            except Exception as db_error:
                logging.warning(f"Failed to save to database: {db_error}")
        else:
            logging.info("DATABASE_URL not set, skipping database save.")
        
        return analysis_result
        
    except Exception as e:
        logging.error(f"Error during analysis: {e}")
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

@app.get("/user/{user_id}/analyses")
async def get_user_analyses(user_id: str, limit: int = 10):
    """
    Busca o histórico de análises de um usuário.
    """
    if not os.getenv("DATABASE_URL"):
        raise HTTPException(status_code=503, detail="Banco de dados não configurado")
    
    try:
        from db import get_user_analyses as db_get_user_analyses
        analyses = await db_get_user_analyses(user_id, limit)
        return {"user_id": user_id, "analyses": analyses}
    except Exception as e:
        logging.error(f"Error fetching user analyses: {e}")
        raise HTTPException(status_code=500, detail=f"Erro ao buscar análises: {str(e)}")

@app.post("/analisar-prato/")
async def analisar_prato(file: UploadFile = File(...)):
    """
    Endpoint simplificado para análise de prato usando Vertex AI.
    
    Recebe uma imagem e retorna análise detalhada do prato usando IA.
    """
    try:
        # Verificar se o arquivo é uma imagem
        if not file.content_type or not file.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="Arquivo deve ser uma imagem")
        
        # Carregar a imagem da requisição
        image_bytes = await file.read()
        
        # Criar o objeto Part para a imagem
        image_part = Part.from_data(data=image_bytes, mime_type=file.content_type)
        
        # Prompt fixo em português
        prompt_texto = "Analise este prato de comida. O que é? Quais são os ingredientes mais prováveis? Forneça uma breve descrição."
        
        # Criar a lista de partes para a requisição
        parts_for_gemini = [image_part, prompt_texto]
        
        # Carregar o modelo Gemini 2.0 Flash (versão mais recente)
        model = GenerativeModel("gemini-2.0-flash-001")
        
        # Fazer a chamada para a API Gemini via Vertex AI
        response = model.generate_content(parts_for_gemini)
        
        # Retornar a resposta da IA
        return {"analise_do_prato": response.text}
        
    except Exception as e:
        logging.error(f"Erro na análise do prato: {e}")
        raise HTTPException(status_code=500, detail=f"Erro ao analisar prato: {str(e)}")
