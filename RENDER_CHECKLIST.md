# ✅ Checklist para Deploy no Render

## 🎯 **Pré-Deploy (Já está pronto!)**

- ✅ **Código funcionando localmente**
- ✅ **requirements.txt** atualizado
- ✅ **render.yaml** configurado  
- ✅ **Dockerfile** criado
- ✅ **.dockerignore** configurado

---

## 🚀 **Passos para Deploy**

### **1. Preparar Repositório GitHub**
```bash
# Na pasta do projeto, execute:
git add .
git commit -m "Ready for Render deploy"
git push origin main
```

### **2. Criar Conta no Render** ✅ (Já aberto no navegador)
- Clique em **"Get Started for Free"**
- Conecte com sua conta do GitHub
- Autorize o Render a acessar seus repositórios

### **3. Criar PostgreSQL Database**
1. No dashboard do Render, clique **"+ New"**
2. Selecione **"PostgreSQL"**
3. Configure:
   - **Name**: `fastscannutri-db`
   - **Database Name**: `fastscannutri`
   - **Region**: `Oregon` (gratuito)
4. Clique **"Create Database"**
5. ⚠️ **IMPORTANTE**: Copie a **Internal Database URL** (vai precisar depois)

### **4. Criar Web Service**
1. Clique **"+ New"** → **"Web Service"**
2. Conecte o repositório `fastscannutri`
3. Configure:
   - **Name**: `fastscannutri-api`
   - **Environment**: `Python 3`
   - **Region**: `Oregon`
   - **Branch**: `main`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### **5. Configurar Variáveis de Ambiente**
Na seção **"Environment Variables"**, adicione:

```
GEMINI_API_KEY = AIzaSyCB_bil7lPowwH5Ngex4aDePJy9b5-5qZ8
DATABASE_URL = (cole aqui a Internal Database URL do PostgreSQL)
PYTHON_VERSION = 3.9.16
```

### **6. Deploy**
1. Clique **"Create Web Service"**
2. Aguarde o build (5-10 minutos)
3. ✅ Quando terminar, você terá uma URL pública!

---

## 🔍 **Verificar se Funcionou**

Sua API estará em: `https://fastscannutri-api.onrender.com`

### Testes:
```bash
# Teste básico
curl https://fastscannutri-api.onrender.com/

# Documentação
# Acesse: https://fastscannutri-api.onrender.com/docs
```

---

## ⚠️ **Pontos Importantes**

### **Hibernação (Plano Gratuito)**
- API hiberna após **15 minutos** de inatividade
- Primeiro request pode demorar **30-60 segundos**
- Normal no plano gratuito!

### **Recursos Gratuitos**
- 512MB RAM
- 100GB bandwidth/mês  
- PostgreSQL: 1GB storage

---

## 🎯 **Próximos Passos Após Deploy**

1. ✅ **Testar a API** com curl ou Postman
2. 🌐 **Atualizar frontend** com nova URL
3. 📊 **Monitorar logs** na aba "Logs"
4. 🔧 **Configurar domínio personalizado** (opcional)

---

## 🆘 **Se Der Problema**

### Build Failed?
- Verificar **"Logs"** no dashboard
- Conferir se `requirements.txt` está correto

### Database Error?
- Usar **Internal Database URL** (não External)
- Verificar se variável `DATABASE_URL` está correta

### API não responde?
- Aguardar 1-2 minutos (pode estar inicializando)
- Verificar logs para erros

---

## 📞 **Links Importantes**

- **Seu Dashboard**: https://dashboard.render.com
- **Documentação**: https://render.com/docs
- **Suporte**: https://render.com/docs/support

---

## 🎉 **Resultado Final**

✅ **API rodando 24/7** em: `https://fastscannutri-api.onrender.com`
✅ **PostgreSQL** configurado e funcionando
✅ **SSL/HTTPS** automático
✅ **Deploy automático** via GitHub
✅ **Documentação** em: `/docs`

**Seu FastScanNutri estará no ar! 🚀**
