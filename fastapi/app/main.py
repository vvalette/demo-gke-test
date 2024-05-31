import asyncpg
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://34.78.238.242"],  # Adjust as necessary
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def get_users_from_db():
    conn = await asyncpg.connect(
        user='test-demo',
        password='test-demo',
        database='postgres',
        host='127.0.0.1',  # Connect to the proxy on localhost
        port=5432
    )
    try:
        users = await conn.fetch("SELECT * FROM users")  # Adjust your query as needed
        return [dict(user) for user in users]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        await conn.close()

@app.get("/users")
async def get_users():
    try:
        users = await get_users_from_db()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
