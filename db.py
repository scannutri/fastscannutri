import os
import asyncpg
import json
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

async def connect_db():
    return await asyncpg.connect(DATABASE_URL)

async def create_table_if_not_exists():
    conn = None
    try:
        conn = await connect_db()
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS analises (
                id SERIAL PRIMARY KEY,
                user_id TEXT NOT NULL,
                nome TEXT,
                resultado JSONB NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        print("Table 'analises' checked/created successfully.")
    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        if conn:
            await conn.close()

async def insert_analysis_result(user_id: str, nome: str, resultado: dict):
    conn = None
    try:
        conn = await connect_db()
        await conn.execute(
            "INSERT INTO analises(user_id, nome, resultado) VALUES($1, $2, $3)",
            user_id, nome, json.dumps(resultado)
        )
        print(f"Analysis result for user {user_id} saved successfully.")
    except Exception as e:
        print(f"Error inserting analysis result: {e}")
    finally:
        if conn:
            await conn.close()

async def get_user_analyses(user_id: str, limit: int = 10):
    """
    Busca as análises de um usuário específico
    """
    DATABASE_URL = os.getenv("DATABASE_URL")
    if not DATABASE_URL:
        raise Exception("DATABASE_URL não configurada")
    
    conn = None
    try:
        conn = await asyncpg.connect(DATABASE_URL)
        
        query = """
        SELECT id, user_id, nome, resultado, created_at 
        FROM analises 
        WHERE user_id = $1 
        ORDER BY created_at DESC 
        LIMIT $2
        """
        
        rows = await conn.fetch(query, user_id, limit)
        
        analyses = []
        for row in rows:
            analyses.append({
                "id": row["id"],
                "user_id": row["user_id"],
                "nome": row["nome"],
                "resultado": row["resultado"],
                "created_at": row["created_at"].isoformat()
            })
        
        return analyses
        
    except Exception as e:
        print(f"Erro ao buscar análises: {e}")
        raise e
    finally:
        if conn:
            await conn.close()


