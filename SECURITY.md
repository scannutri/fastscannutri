# 🔒 INSTRUÇÕES DE SEGURANÇA - CREDENCIAIS GOOGLE CLOUD

## ⚠️ ALERTA DE SEGURANÇA

Este projeto utiliza credenciais do Google Cloud Service Account para acessar as APIs do Vertex AI. **NUNCA** commite estes arquivos no Git!

## ✅ Configuração Segura das Credenciais

### 1. Localização das Credenciais
- ✅ **Correto**: `/Users/vini.mqs/google-credentials-fastscannutri.json` (fora do projeto)
- ❌ **PERIGOSO**: `./google-credentials.json` (dentro do projeto)

### 2. Arquivo .env
O arquivo `.env` contém o caminho para as credenciais:
```bash
GOOGLE_APPLICATION_CREDENTIALS=/Users/vini.mqs/google-credentials-fastscannutri.json
```

### 3. .gitignore
Os seguintes arquivos estão sendo ignorados pelo Git:
```
.env
.env.*
google-credentials.json
*.json
```

## 🚨 Se as Credenciais foram Expostas

Se você suspeia que as credenciais foram commitadas no Git ou expostas:

1. **Revogue as credenciais imediatamente** no Google Cloud Console
2. **Gere novas credenciais** para o service account
3. **Verifique o histórico do Git** para remover commits com credenciais
4. **Monitore sua conta** para atividades suspeitas

## 📝 Comandos para Verificar Segurança

```bash
# Verificar se credenciais não estão no Git
git log --oneline --grep="credentials"

# Verificar se arquivos estão sendo ignorados
git status --ignored

# Verificar se .env existe mas não está sendo rastreado
ls -la .env*
git status .env
```

## 🔧 Para Desenvolvimento Local

1. Certifique-se de que o arquivo de credenciais está fora do projeto
2. Configure a variável de ambiente `GOOGLE_APPLICATION_CREDENTIALS` no arquivo `.env`
3. Nunca inclua credenciais diretamente no código

## 🌐 Para Produção (Render)

Use variáveis de ambiente no painel do Render:
- `GOOGLE_APPLICATION_CREDENTIALS` → conteúdo completo do arquivo JSON
- `VERTEX_AI_PROJECT_ID` → ID do projeto
- `VERTEX_AI_LOCATION` → localização da API

---
**Data da Correção**: 11 de agosto de 2025
**Status**: ✅ Credenciais movidas para local seguro
