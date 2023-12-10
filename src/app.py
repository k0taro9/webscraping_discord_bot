import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN_SECRET = os.getenv("DISCORD_TOKEN")