# 🚀 Deploy no Railway - Passo a Passo

## Por que Railway?
- ✅ **Gratuito** até $5/mês de uso
- ✅ **PostgreSQL incluído** sem custo extra
- ✅ **Deploy automático** via GitHub
- ✅ **SSL/HTTPS** automático
- ✅ **Logs em tempo real**
- ✅ **Fácil de usar**

---

## 📋 Pré-requisitos
- Conta no GitHub (para conectar o repositório)
- Projeto FastScanNutri funcionando localmente

---

## 🔥 Passo a Passo

### 1. **Preparar o Repositório**
```bash
# Na pasta do projeto
git init
git add .
git commit -m "Initial commit - FastScanNutri API"

# Criar repositório no GitHub e fazer push
git remote add origin https://github.com/SEU_USUARIO/fastscannutri.git
git push -u origin main
```

### 2. **Criar Conta no Railway**
1. Acesse: https://railway.app
2. Clique em **"Start a New Project"**
3. Conecte sua conta do GitHub
4. Autorize o Railway a acessar seus repositórios

### 3. **Fazer Deploy do Projeto**
1. Clique em **"Deploy from GitHub repo"**
2. Selecione o repositório `fastscannutri`
3. Railway detectará automaticamente que é um projeto Python/FastAPI

### 4. **Configurar Variáveis de Ambiente**
1. No dashboard do projeto, vá em **"Variables"**
2. Adicione as variáveis:
   ```
   GEMINI_API_KEY=sua_chave_gemini_aqui
   ```

### 5. **Adicionar PostgreSQL**
1. Clique em **"+ New"** no dashboard
2. Selecione **"Database"** → **"PostgreSQL"**
3. Railway criará um banco automaticamente
4. A variável `DATABASE_URL` será configurada automaticamente

### 6. **Verificar Deploy**
1. Railway fará o build automaticamente
2. Quando terminar, você receberá uma URL pública
3. Exemplo: `https://seu-projeto.railway.app`

### 7. **Testar a API**
```bash
# Teste básico
curl https://seu-projeto.railway.app/

# Teste com a documentação
# Acesse: https://seu-projeto.railway.app/docs
```

---

## ⚙️ **Configurações Avançadas**

### Domínio Personalizado
1. Vá em **"Settings"** → **"Domains"**
2. Adicione seu domínio personalizado
3. Configure o DNS apontando para Railway

### Logs e Monitoramento
1. Aba **"Logs"** - Ver logs em tempo real
2. Aba **"Metrics"** - CPU, memória, requests

### Auto-redeploy
- Railway faz redeploy automático a cada push no GitHub
- Para desabilitar: **Settings** → **"Auto Deploy"** → Off

---

## 🔍 **Troubleshooting**

### Build falha?
```bash
# Verifique se requirements.txt está correto
pip freeze > requirements.txt
```

### Erro de conexão com banco?
- Verifique se a variável `DATABASE_URL` está configurada
- Railway configura automaticamente quando adiciona PostgreSQL

### API não responde?
- Verifique os logs na aba "Logs"
- Certifique-se que está usando `--host 0.0.0.0` no uvicorn

---

## 💰 **Custos**

### Plano Gratuito:
- **$5.00 de crédito gratuito por mês**
- Suficiente para desenvolvimento e testes
- PostgreSQL incluído

### Como economizar:
- Use sleep mode para ambientes de desenvolvimento
- Monitore uso na aba "Usage"

---

## 🎯 **Próximos Passos**

1. ✅ Deploy realizado
2. ✅ API funcionando em produção
3. 📱 Atualizar URL no frontend
4. 🔧 Configurar monitoramento
5. 🚀 Adicionar features novas

---

## 📞 **Links Úteis**

- **Dashboard**: https://railway.app/dashboard
- **Documentação**: https://docs.railway.app
- **Suporte**: https://help.railway.app
- **Status**: https://status.railway.app

---

## 🎉 **Resultado Final**

Sua API estará disponível 24/7 em uma URL como:
`https://fastscannutri-production.railway.app`

E você poderá acessar a documentação em:
`https://fastscannutri-production.railway.app/docs`
