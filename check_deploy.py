#!/usr/bin/env python3
"""
Script para verificar se tudo está configurado corretamente antes do deploy
"""
import os
import json
from dotenv import load_dotenv

def check_environment():
    print("🔍 Verificando configuração para deploy no Render...")
    
    # Carregar .env para teste local
    load_dotenv()
    
    issues = []
    
    # Verificar variáveis essenciais
    vertex_project = os.getenv("VERTEX_AI_PROJECT_ID")
    if not vertex_project:
        issues.append("❌ VERTEX_AI_PROJECT_ID não configurado")
    else:
        print(f"✅ VERTEX_AI_PROJECT_ID: {vertex_project}")
    
    credentials = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if not credentials:
        issues.append("❌ GOOGLE_APPLICATION_CREDENTIALS não configurado")
    elif credentials.startswith("{"):
        try:
            json.loads(credentials)
            print("✅ GOOGLE_APPLICATION_CREDENTIALS: JSON válido")
        except json.JSONDecodeError:
            issues.append("❌ GOOGLE_APPLICATION_CREDENTIALS: JSON inválido")
    else:
        if os.path.exists(credentials):
            print(f"✅ GOOGLE_APPLICATION_CREDENTIALS: {credentials} (arquivo existe)")
        else:
            issues.append(f"❌ GOOGLE_APPLICATION_CREDENTIALS: {credentials} (arquivo não encontrado)")
    
    # Verificar arquivos essenciais
    essential_files = [
        "main.py", "model.py", "db.py", 
        "requirements.txt", "render.yaml", "apt.txt"
    ]
    
    for file in essential_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            issues.append(f"❌ {file} não encontrado")
    
    # Resultado
    if issues:
        print("\n🚨 PROBLEMAS ENCONTRADOS:")
        for issue in issues:
            print(f"  {issue}")
        print("\n❌ Corrija os problemas antes de fazer deploy!")
        return False
    else:
        print("\n🎉 Tudo OK! Pronto para deploy no Render!")
        return True

if __name__ == "__main__":
    check_environment()
