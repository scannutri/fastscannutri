# 🍎 FastScanNutri API

API de análise nutricional com IA usando Google Vertex AI.

## 🚀 Deploy no Render

### Variáveis de ambiente necessárias:
```
VERTEX_AI_PROJECT_ID=gen-lang-client-0606566455
GOOGLE_APPLICATION_CREDENTIALS={"type":"service_account",...}
DATABASE_URL=postgresql://... (opcional)
```

### Comandos:
- **Build**: `pip install -r requirements.txt`  
- **Start**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

## 📚 Endpoints

- `POST /analyze` - Análise de imagem
- `GET /health` - Health check
- `GET /docs` - Documentação

## 🛠️ Arquivos essenciais

- `main.py` - Aplicação principal
- `model.py` - Modelos Pydantic  
- `db.py` - Banco de dados
- `requirements.txt` - Dependências
- `render.yaml` - Configuração do Render
- `.env.example` - Exemplo de configuração

- 📸 **Análise de imagens de alimentos** usando Vertex AI (Gemini 2.0 Flash)
- 🔢 **Cálculo automático** de calorias, proteínas, carboidratos e gorduras
- 📊 **Estimativas por intervalos** (min-max) para maior precisão
- 💾 **Histórico de análises** salvo em PostgreSQL
- 🌐 **API REST** com documentação automática
- ⚡ **Deploy fácil** no Render

## 🛠️ Tecnologias

- **FastAPI** - Framework web moderno e rápido
- **Google Vertex AI** - IA para análise de imagens (Gemini 2.0 Flash)
- **PostgreSQL** - Banco de dados para histórico
- **Pydantic** - Validação de dados
- **Docker** - Containerização

## 📋 Endpoints

- `POST /analyze` - Análise nutricional completa de imagem
- `POST /analisar-prato/` - Análise simples de prato
- `GET /health` - Status da API
- `GET /user/{user_id}/analyses` - Histórico do usuário
- `GET /docs` - Documentação interativa

## 🔧 Instalação Local

### Pré-requisitos
- Python 3.9+
- PostgreSQL (ou usar banco externo)
- Google Cloud Project com Vertex AI habilitado

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/fastscannutri.git
cd fastscannutri
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure as credenciais do Google Cloud

**⚠️ IMPORTANTE: As credenciais são sensíveis e NÃO devem ser commitadas!**

#### Opção A: Service Account Key (Recomendado)
1. Crie um Service Account no Google Cloud Console
2. Baixe o arquivo JSON de credenciais
3. Salve como `google-credentials.json` na raiz do projeto
4. O arquivo já está no `.gitignore` e não será commitado

#### Opção B: Application Default Credentials
```bash
gcloud auth application-default login
```

### 4. Configure as variáveis de ambiente
```bash
cp .env.example .env
# Edite o .env com suas configurações
```

**Exemplo do .env:**
```env
VERTEX_AI_PROJECT_ID=seu-project-id-gcp
VERTEX_AI_LOCATION=us-central1
GOOGLE_APPLICATION_CREDENTIALS=./google-credentials.json
DATABASE_URL=sua-url-do-banco
```
```

### 4. Execute a aplicação
```bash
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`

## 🌐 Deploy

### Render (Recomendado)
1. Conecte este repositório ao [Render](https://render.com)
2. Configure as variáveis de ambiente:
   - `GEMINI_API_KEY` - Sua chave do Google Gemini
   - `DATABASE_URL` - URL do PostgreSQL (Render cria automaticamente)

### Docker
```bash
docker build -t fastscannutri .
docker run -p 8000:8000 -e GEMINI_API_KEY=sua_chave fastscannutri
```

## 📖 Exemplo de Uso

### JavaScript/Frontend
```javascript
const formData = new FormData();
formData.append('image', imageFile);
formData.append('user_id', 'user123');

const response = await fetch('/analyze', {
    method: 'POST',
    body: formData
});

const analysis = await response.json();
console.log(analysis);
```

### Resposta da API
```json
{
  "overview": "Prato com arroz, feijão e frango grelhado",
  "short_name": "Prato feito completo",
  "items": [
    {
      "name": "Arroz branco",
      "type": "carb",
      "portion_size": "1 xícara",
      "macros_g": {
        "protein": 4.0,
        "carbs": 45.0,
        "fat": 0.5
      },
      "calories_kcal": {
        "low": 200,
        "high": 220
      }
    }
  ],
  "total_calories_kcal": {
    "low": 650,
    "high": 750
  },
  "total_macros": {
    "proteins": { "low": 35.0, "high": 45.0 },
    "carbs": { "low": 60.0, "high": 75.0 },
    "fat": { "low": 15.0, "high": 25.0 }
  }
}
```

## 🔑 Obtendo Chave do Gemini

1. Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Crie uma nova API Key
3. Adicione no arquivo `.env` como `GEMINI_API_KEY=sua_chave`

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🤝 Contribuição

Contribuições são bem-vindas! Abra uma issue ou envie um pull request.

---

**Desenvolvido com ❤️ para análise nutricional inteligente**
