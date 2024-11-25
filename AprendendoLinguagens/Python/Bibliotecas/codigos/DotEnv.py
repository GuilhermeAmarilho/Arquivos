from dotenv import load_dotenv, dotenv_values

load_dotenv()

# ├── .env
# └── foo.py

config = dotenv_values(".env")
# config = {"USER": "foo", "EMAIL": "foo@example.org"}
