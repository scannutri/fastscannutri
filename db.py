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


