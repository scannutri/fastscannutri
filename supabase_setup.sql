-- Script SQL para configurar a tabela 'analises' no Supabase
-- Execute este script no SQL Editor do Supabase

-- Criar a tabela analises
CREATE TABLE IF NOT EXISTS analises (
  id SERIAL PRIMARY KEY,
  user_id TEXT NOT NULL,
  nome TEXT,
  resultado JSONB NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Adicionar índices para melhor performance
CREATE INDEX IF NOT EXISTS idx_analises_user_id ON analises(user_id);
CREATE INDEX IF NOT EXISTS idx_analises_created_at ON analises(created_at);

-- Opcional: Adicionar RLS (Row Level Security) se necessário
-- ALTER TABLE analises ENABLE ROW LEVEL SECURITY;

-- Verificar se a tabela foi criada
SELECT table_name, column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'analises' 
ORDER BY ordinal_position;
