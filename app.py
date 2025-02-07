import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print("Pinecone API Key:", PINECONE_API_KEY)
print("OpenAI API Key:", OPENAI_API_KEY)
