
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

client = MongoClient('mongodb://localhost:27017/')
db = client['rule_engine_db']

from .main import app
