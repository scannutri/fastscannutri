# 🚀 Configuração do Supabase para FastScanNutri

## 📋 Passos para Configurar o Supabase

### 1. Criar Conta e Projeto no Supabase
1. Acesse [supabase.com](https://supabase.com)
2. Crie uma conta ou faça login
3. Clique em "New Project"
4. Escolha sua organização
5. Preencha:
   - **Name**: FastScanNutri (ou nome de sua escolha)
   - **Database Password**: Crie uma senha forte (anote ela!)
   - **Region**: Escolha a região mais próxima
6. Clique em "Create new project"
7. Aguarde alguns minutos para o projeto ser criado

### 2. Obter a String de Conexão
1. No painel do projeto, vá em **Project Settings** (⚙️)
2. Clique em **Database** na barra lateral
3. Role até a seção **Connection string**
4. Copie a string que começa com `postgresql://postgres:...`
5. A string será algo como:
   ```
   postgresql://postgres:[YOUR-PASSWORD]@db.[YOUR-PROJECT-REF].supabase.co:5432/postgres
   ```

### 3. Atualizar o arquivo .env
1. Abra o arquivo `.env` no seu projeto
2. Substitua `[YOUR-PASSWORD]` pela senha que você criou
3. Substitua `[YOUR-PROJECT-REF]` pelo ID do seu projeto
4. Exemplo final:
   ```
   DATABASE_URL=postgresql://postgres:minhasenha123@db.abcdefghijklmnop.supabase.co:5432/postgres
   ```

### 4. Criar a Tabela no Supabase
1. No painel do Supabase, vá em **SQL Editor**
2. Clique em **New query**
3. Copie e cole o conteúdo do arquivo `supabase_setup.sql`
4. Clique em **Run** para executar
5. Verifique se a tabela foi criada em **Table Editor**

### 5. Testar a Aplicação
```bash
# Reiniciar o servidor FastAPI
/Users/vini.mqs/Documents/fastscannutri/.venv/bin/uvicorn main:app --reload --port 8001
```

## 🔧 Informações Importantes

### URLs do Projeto Supabase
- **Project URL**: `https://[YOUR-PROJECT-REF].supabase.co`
- **API URL**: `https://[YOUR-PROJECT-REF].supabase.co/rest/v1/`
- **Anon Key**: Disponível em Project Settings > API

### Vantagens do Supabase
- ✅ PostgreSQL gerenciado na nuvem
- ✅ Backup automático
- ✅ Interface visual para gerenciar dados
- ✅ API REST automática
- ✅ Escalabilidade automática
- ✅ SSL/TLS integrado

### Troubleshooting
- Se der erro de conexão, verifique se a string está correta
- Certifique-se de que a senha não contém caracteres especiais que precisam ser escapados
- O Supabase tem um firewall básico, mas geralmente permite conexões de qualquer lugar

## 📞 Próximos Passos
1. Siga as instruções acima
2. Teste a aplicação acessando `http://127.0.0.1:8001/docs`
3. Faça um teste de análise nutricional
4. Verifique se os dados estão sendo salvos no Supabase em **Table Editor**
