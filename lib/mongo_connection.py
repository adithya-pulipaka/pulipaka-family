import os
from pymongo import AsyncMongoClient
from dotenv import load_dotenv

load_dotenv()

client: AsyncMongoClient | None = None

async def connect_to_mongo():
    global client
    client = AsyncMongoClient(os.environ["MONGODB_URL"])
    try:
        # Ping the database to check the connection
        await client.admin.command('ping')
        print("Connected to MongoDB!")
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        client = None

async def close_mongo_connection():
    global client
    if client:
        await client.close()
        print("Closed MongoDB connection.")

def get_mongo_client() -> AsyncMongoClient:
    return client


