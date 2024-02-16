import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("TOKEN")
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC')
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
