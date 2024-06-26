import asyncpg
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as necessary
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def get_users_from_db():
    conn = await asyncpg.connect(
        user='test-demo',
        password='test-demo',
        database='my_database',
        host='127.0.0.1',
        port=5432
    )
    users = await conn.fetch("SELECT * FROM users")  # Adjust your query as needed
    return [dict(user) for user in users]


@app.get("/users")
async def get_users():
        users = await get_users_from_db()
        return users

