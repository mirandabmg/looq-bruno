import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do banco de dados MySQL
DB_USER = os.getenv("DB_USER", "looqbox-challenge")
DB_PASSWORD = os.getenv("DB_PASSWORD", "looq-challenge")
DB_HOST = os.getenv("DB_HOST", "35.199.115.174")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "looqbox_challenge")

# String de conexão MySQL
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
