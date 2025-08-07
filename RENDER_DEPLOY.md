# 🔵 Deploy no Render - Passo a Passo

## Por que Render?
- ✅ **750 horas gratuitas** por mês
- ✅ **PostgreSQL gratuito** incluído
- ✅ **SSL/HTTPS** automático
- ✅ **Deploy via GitHub** automático
- ⚠️ **Hiberna após 15min** de inatividade (plano gratuito)

---

## 🚀 Passo a Passo

### 1. **Preparar Repositório GitHub**
```bash
# Se ainda não fez:
git init
git add .
git commit -m "FastScanNutri API ready for deploy"
git push origin main
```

### 2. **Criar Conta no Render**
1. Acesse: https://render.com
2. Clique em **"Get Started for Free"**
3. Conecte com GitHub

### 3. **Criar Web Service**
1. No dashboard, clique **"+ New"** → **"Web Service"**
2. Conecte seu repositório GitHub `fastscannutri`
3. Configure:
   - **Name**: `fastscannutri-api`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### 4. **Configurar Variáveis de Ambiente**
Na seção **"Environment Variables"**:
```
GEMINI_API_KEY = sua_chave_gemini_aqui
PYTHON_VERSION = 3.9.16
```

### 5. **Criar PostgreSQL Database**
1. Clique **"+ New"** → **"PostgreSQL"**
2. Configure:
   - **Name**: `fastscannutri-db`
   - **Database Name**: `fastscannutri`
   - **User**: `postgres`
3. Clique **"Create Database"**

### 6. **Conectar Database ao Web Service**
1. Volte ao Web Service
2. Em **Environment Variables**, adicione:
   ```
   DATABASE_URL = (copie a Internal Database URL do PostgreSQL criado)
   ```

### 7. **Deploy**
1. Clique **"Create Web Service"**
2. Render iniciará o build automaticamente
3. Aguarde o deploy (5-10 minutos)

---

## 🔧 **Configurações Importantes**

### Auto-Deploy
- Deploy automático a cada push no GitHub
- Para desabilitar: **Settings** → **Auto-Deploy** → Off

### Scaling
- **Plano gratuito**: 1 instância, 512MB RAM
- **Plano pago**: Multiple instances, mais RAM

### Health Check
Render verifica automaticamente se sua API responde em `/`

---

## ⚠️ **Limitações do Plano Gratuito**

### Sleep Mode
- API **hiberna após 15 minutos** de inatividade
- Primeiro request após hibernar pode demorar 30-60 segundos
- Para evitar: faça requests periódicos ou upgrade para plano pago

### Recursos
- **512MB RAM**
- **100GB bandwidth/mês**
- **750 horas/mês** (suficiente para uso normal)

---

## 🎯 **URLs de Acesso**

Sua API ficará disponível em:
```
https://fastscannutri-api.onrender.com
```

Documentação:
```
https://fastscannutri-api.onrender.com/docs
```

---

## 🔍 **Troubleshooting**

### Build Failed?
- Verifique se `requirements.txt` está completo
- Logs disponíveis na aba **"Logs"**

### Database Connection Error?
- Verifique se `DATABASE_URL` está correta
- Use a **Internal Database URL** (não External)

### API Slow to Respond?
- Plano gratuito hiberna após inatividade
- Considere upgrade ou use keep-alive service

---

## 💰 **Custos**

### Gratuito:
- Web Service: 750 horas/mês
- PostgreSQL: 1GB storage, 1 milhão de rows

### Paid Plans:
- **Starter**: $7/mês (sem hibernação)
- **Standard**: $25/mês (mais recursos)

---

## 🎉 **Vantagens do Render**

1. ✅ **Fácil de usar**
2. ✅ **PostgreSQL gratuito**
3. ✅ **SSL automático**
4. ✅ **Logs em tempo real**
5. ✅ **Custom domains**
6. ✅ **Auto-scaling**

---

## 📞 **Links Úteis**

- **Dashboard**: https://dashboard.render.com
- **Docs**: https://render.com/docs
- **Status**: https://status.render.com
- **Community**: https://community.render.com

---

## 🚀 **Resultado Final**

✅ API rodando 24/7 (com hibernação no plano gratuito)
✅ PostgreSQL configurado
✅ HTTPS automático
✅ Deploy automático via GitHub
✅ Monitoramento e logs incluídos

**URL da sua API**: `https://fastscannutri-api.onrender.com`
