import os
from dotenv import load_dotenv
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import logging

load_dotenv()

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
from utils import call_gemini_vision_api
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
            "gemini_api": "unknown"
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
    
    # Verificar Gemini API Key
    try:
        if os.getenv("GEMINI_API_KEY"):
            health_status["services"]["gemini_api"] = "configured"
        else:
            health_status["services"]["gemini_api"] = "not_configured"
            health_status["status"] = "degraded"
    except Exception as e:
        health_status["services"]["gemini_api"] = "error"
        health_status["status"] = "degraded"
    
    return health_status

@app.post("/analyze", response_model=GeminiVisionResponse)
async def analyze_image(
    image: UploadFile = File(..., description="Imagem do alimento para análise"),
    user_id: str = Form(..., description="ID único do usuário"),
    nome: str = Form(None, description="Nome do alimento (opcional)")
):
    """
    Analisa uma imagem de alimento e retorna informações nutricionais detalhadas.
    
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
        
        # Chamar a API do Gemini
        gemini_response_data = call_gemini_vision_api(image_data, image.content_type)
        logging.info("Gemini API called successfully.")
        
        # Validar e converter a resposta para o modelo Pydantic
        analysis_result = GeminiVisionResponse(**gemini_response_data)
        logging.info("Gemini response parsed and validated.")
        
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
