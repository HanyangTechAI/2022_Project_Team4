from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    default_dir = os.environ.get('DEFAULT_DIR')

config = Config()