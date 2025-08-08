#!/usr/bin/env python3
"""
Script de inicialização para o deploy no Render
Inicializa o banco de dados antes de iniciar o servidor
"""
import asyncio
import os
import sys
from dotenv import load_dotenv
from db import create_table_if_not_exists

async def init_app():
    """Inicializa a aplicação"""
    print("🚀 Inicializando FastScanNutri API...")
    
    # Carrega variáveis de ambiente
    load_dotenv()
    
    # Verifica se as variáveis essenciais estão configuradas
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    database_url = os.getenv("DATABASE_URL")
    
    if not gemini_api_key:
        print("❌ GEMINI_API_KEY não configurada")
        sys.exit(1)
        
    if not database_url:
        print("❌ DATABASE_URL não configurada")
        sys.exit(1)
    
    print("✅ Variáveis de ambiente configuradas")
    
    # Inicializa o banco de dados
    try:
        await create_table_if_not_exists()
        print("✅ Banco de dados inicializado")
    except Exception as e:
        print(f"❌ Erro ao inicializar banco de dados: {e}")
        sys.exit(1)
    
    print("🎉 FastScanNutri API inicializada com sucesso!")

if __name__ == "__main__":
    asyncio.run(init_app())
