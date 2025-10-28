import os
from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase
from dotenv import load_dotenv
import certifi

load_dotenv()

client: AsyncMongoClient | None = None
db: AsyncDatabase | None = None

async def connect_mongo():
    global client
    global db
    client = AsyncMongoClient(os.environ["MONGODB_URL"].format(certifi.where()))
    try:
        await client.admin.command('ping')
        print("Connected to MongoDB!")
        db = client.get_database(os.environ["DB_NAME"])

    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        client = None

async def close_mongo():
    global client
    if client:
        await client.close()
        print("Closed MongoDB connection.")

async def get_mongo_db() -> AsyncDatabase:
    return db


