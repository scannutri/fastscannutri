# 🚀 Guia de Deploy - FastScanNutri API

## 📋 Opções de Deploy

### 1. 🌐 **Railway** (Recomendado - Fácil e Gratuito)
### 2. 🔵 **Render** (Gratuito com limitações)
### 3. ☁️ **Heroku** (Pago, mas confiável)
### 4. 🐳 **Docker + VPS** (Controle total)
### 5. ⚡ **Vercel** (Para APIs simples)

---

## 🚀 **Option 1: Railway (Recomendado)**

### Por que Railway?
- ✅ Deploy gratuito até $5/mês
- ✅ PostgreSQL gratuito incluído
- ✅ Deploy automático via Git
- ✅ SSL/HTTPS automático
- ✅ Logs em tempo real

### Passos:
1. **Acesse**: https://railway.app
2. **Conecte seu GitHub**: Faça upload do projeto
3. **Configure variáveis**: Adicione `GEMINI_API_KEY`
4. **Deploy automático**: Railway detecta FastAPI automaticamente

---

## 🔵 **Opção 2: Render**

### Vantagens:
- ✅ 750 horas gratuitas/mês
- ✅ PostgreSQL gratuito
- ✅ SSL automático
- ⚠️ Hiberna após inatividade (plano gratuito)

### Passos:
1. **Acesse**: https://render.com
2. **Conecte repositório**: GitHub/GitLab
3. **Configure build**: Detecta automaticamente
4. **Adicione variáveis**: Environment variables

---

## ☁️ **Opção 3: Heroku**

### Características:
- 💰 Pago (a partir de $7/mês)
- ✅ Muito confiável
- ✅ Add-ons (PostgreSQL, Redis, etc.)
- ✅ CI/CD integrado

---

## 🐳 **Opção 4: Docker + VPS**

### Para quem quer controle total:
- VPS (DigitalOcean, Linode, AWS EC2)
- Docker container
- Nginx reverse proxy
- SSL com Let's Encrypt

---

## ⚡ **Opção 5: Vercel**

### Limitações:
- ⚠️ Melhor para APIs serverless simples
- ⚠️ Timeout de 10s (pode ser problema para IA)
- ✅ Deploy super fácil

---

## 📦 **Arquivos Necessários (já criados)**

- `requirements.txt` - Dependências Python
- `Dockerfile` - Para containerização
- `railway.json` - Configuração Railway
- `render.yaml` - Configuração Render
- `Procfile` - Para Heroku
- `vercel.json` - Para Vercel
- `.dockerignore` - Arquivos a ignorar no Docker

---

## 🔧 **Configuração de Ambiente**

### Variáveis obrigatórias:
```
GEMINI_API_KEY=sua_chave_aqui
DATABASE_URL=sua_url_do_banco
```

### Variáveis opcionais:
```
PORT=8000
PYTHONPATH=/app
```

---

## 🎯 **Recomendação**

**Para começar**: Use **Railway** (mais fácil)
**Para produção**: Use **Railway** ou **Render** 
**Para escala**: Use **Docker + VPS**

---

## 📞 **Próximos Passos**

1. Escolha uma plataforma
2. Siga o guia específico
3. Configure as variáveis
4. Teste o deploy
5. Atualize a URL no frontend
