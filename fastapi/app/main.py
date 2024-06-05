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

# Get the Cloud SQL connection name from the environment variable
CLOUD_SQL_CONNECTION_NAME = os.environ.get("CLOUD_SQL_CONNECTION_NAME")

async def get_users_from_db():
    # Connect to Cloud SQL using the connection name
    conn = await asyncpg.connect(CLOUD_SQL_CONNECTION_NAME)
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
