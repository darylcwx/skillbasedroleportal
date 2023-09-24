import os
from dotenv import load_dotenv

load_dotenv()

# Establish MySQL connection
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")

db= 'SBRP_Ais_Kachang'

db_uri = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"


