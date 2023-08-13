# config.py

from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR =  BASE_DIR / 'data'
LOG_DIR = BASE_DIR / 'logs'

# API keys
API_KEY = 'abcd'