import os
from dotenv import load_dotenv

class Config:
    FILE_PATH = os.getcwd() + "/datas/example.pdf"
    DB_PATH = os.getcwd() + "/db"