# 🍎 FastScanNutri API

API de análise nutricional inteligente usando Google Gemini AI para identificar alimentos em imagens e calcular informações nutricionais.

## 🚀 Funcionalidades

- 📸 **Análise de imagens de alimentos** usando IA do Google Gemini
- 🔢 **Cálculo automático** de calorias, proteínas, carboidratos e gorduras
- 📊 **Estimativas por intervalos** (min-max) para maior precisão
- 💾 **Histórico de análises** salvo em PostgreSQL
- 🌐 **API REST** com documentação automática
- ⚡ **Deploy fácil** com Docker e Render

## 🛠️ Tecnologias

- **FastAPI** - Framework web moderno e rápido
- **Google Gemini 1.5 Flash** - IA para análise de imagens
- **PostgreSQL** - Banco de dados para histórico
- **Pydantic** - Validação de dados
- **Docker** - Containerização

## 📋 Endpoints

- `POST /analyze` - Análise nutricional de imagem
- `GET /health` - Status da API
- `GET /user/{user_id}/analyses` - Histórico do usuário
- `GET /docs` - Documentação interativa

## 🔧 Instalação Local

### Pré-requisitos
- Python 3.9+
- PostgreSQL (ou Docker)
- Chave da API do Google Gemini

### 1. Clone o repositório
```bash
git clone https://github.com/scannutri/fastscannutri.git
cd fastscannutri
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente
```bash
cp .env.example .env
# Edite o .env com suas chaves
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
