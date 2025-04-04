from dotenv import load_dotenv
import os

load_dotenv(".env")

DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")

# DATABASE_URL = f"postgres://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DATABASE_URL = "postgresql://neondb_owner:npg_CX0PouQLw1vH@ep-divine-sun-a1fx39xw-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require"


