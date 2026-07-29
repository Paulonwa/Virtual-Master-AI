import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

DATABASE_NAME = "virtualmaster.db"

LEAGUE_NAME = "SportyBet Scheduled Virtual League"

VERSION = "0.1.0"
