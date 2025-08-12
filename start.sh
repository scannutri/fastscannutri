#!/bin/bash

# Script de inicialização para produção no Render
set -e

echo "🚀 Starting FastScanNutri API..."

# Verificar variáveis essenciais
if [ -z "$VERTEX_AI_PROJECT_ID" ]; then
    echo "❌ ERROR: VERTEX_AI_PROJECT_ID is not set"
    exit 1
fi

if [ -z "$GOOGLE_APPLICATION_CREDENTIALS" ]; then
    echo "❌ ERROR: GOOGLE_APPLICATION_CREDENTIALS is not set"
    exit 1
fi

echo "✅ Environment variables checked"

# Verificar se é uma string JSON ou path
if [[ "$GOOGLE_APPLICATION_CREDENTIALS" == "{"* ]]; then
    echo "📝 Writing Google credentials to temporary file..."
    echo "$GOOGLE_APPLICATION_CREDENTIALS" > /tmp/google-credentials.json
    export GOOGLE_APPLICATION_CREDENTIALS="/tmp/google-credentials.json"
    echo "✅ Google credentials configured"
fi

# Iniciar a aplicação
echo "🌟 Starting uvicorn server..."
exec uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000} --workers 1 --access-log
