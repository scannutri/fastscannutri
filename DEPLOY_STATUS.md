# 🚀 Guia de Deploy - FastScanNutri API

## ✅ Status do Projeto

O projeto está **PRONTO PARA DEPLOY** no Render com banco PostgreSQL externo!

### 🔧 Configurações Realizadas

- ✅ Banco de dados PostgreSQL externo conectado e testado
- ✅ Tabela `analises` criada automaticamente
- ✅ Variáveis de ambiente configuradas
- ✅ Endpoints funcionais testados
- ✅ Arquivos de deploy preparados

## 📋 Passos para Deploy no Render

### 1. Upload para GitHub

```bash
# Se ainda não foi feito:
git add .
git commit -m "Configuração final para deploy com banco externo"
git push origin main
```

### 2. Deploy no Render

1. Acesse [https://render.com](https://render.com)
2. Conecte seu repositório GitHub: `https://github.com/scannutri/fastscannutri.git`
3. Configure o Web Service:
   - **Name**: `fastscannutri-api`
   - **Environment**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: Free

### 3. Configurar Variáveis de Ambiente

No dashboard do Render, adicione estas variáveis:

```
GEMINI_API_KEY=AIzaSyCB_bil7lPowwH5Ngex4aDePJy9b5-5qZ8
DATABASE_URL=postgresql://vinicius:Ap83JBtZSFE95S33jWhxYzP7hwstIo8Z@dpg-d2b7g6qdbo4c73aiuh40-a.oregon-postgres.render.com/scannutri
```

### 4. Testar o Deploy

Após o deploy, teste os endpoints:

```bash
# Endpoint principal
curl https://seu-app.onrender.com/

# Health check
curl https://seu-app.onrender.com/health

# Documentação automática
https://seu-app.onrender.com/docs
```

## 🔗 URLs do Projeto

- **Repositório**: https://github.com/scannutri/fastscannutri.git
- **Deploy URL**: `https://seu-app.onrender.com` (será gerada após deploy)
- **Documentação**: `https://seu-app.onrender.com/docs`

## 🧪 Exemplo de Teste da API

### Análise de Imagem (Frontend)

```javascript
const formData = new FormData();
formData.append('file', imageFile);
formData.append('user_id', 'user123');

fetch('https://seu-app.onrender.com/analyze', {
    method: 'POST',
    body: formData
})
.then(response => response.json())
.then(data => console.log(data));
```

### Buscar Histórico de Análises

```javascript
fetch('https://seu-app.onrender.com/user/user123/analyses')
.then(response => response.json())
.then(data => console.log('Histórico:', data));
```

## 📊 Banco de Dados

### Detalhes da Conexão
- **Host**: `dpg-d2b7g6qdbo4c73aiuh40-a.oregon-postgres.render.com`
- **Database**: `scannutri`
- **User**: `vinicius`
- **Status**: ✅ Conectado e testado

### Estrutura da Tabela `analises`
```sql
CREATE TABLE analises (
    id SERIAL PRIMARY KEY,
    user_id TEXT NOT NULL,
    nome TEXT,
    resultado JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 📱 Integração com Frontend

### Endpoints Disponíveis

1. **GET /** - Página inicial
2. **GET /health** - Status da API
3. **POST /analyze** - Análise de imagem
4. **GET /user/{user_id}/analyses** - Histórico do usuário
5. **GET /docs** - Documentação interativa

### Formato de Resposta da Análise

```json
{
    "calorias_totais": 350,
    "proteinas": 15,
    "carboidratos": 45,
    "fibras": 8,
    "gorduras_totais": 12,
    "gorduras_saturadas": 3,
    "acucar": 10,
    "sodio": 200,
    "ingredientes_identificados": ["banana", "aveia", "leite"],
    "observacoes": "Lanche saudável e nutritivo...",
    "recomendacoes": "Boa opção para café da manhã..."
}
```

## 🔄 Próximos Passos

1. **Fazer o deploy no Render**
2. **Testar a API em produção**
3. **Integrar com o frontend**
4. **Monitorar performance e logs**

## 📞 Suporte

- Logs do Render: Dashboard > Logs
- Documentação API: `/docs`
- Status da aplicação: `/health`

---

**Status**: ✅ PRONTO PARA DEPLOY
**Data**: $(date)
