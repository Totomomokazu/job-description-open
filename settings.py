import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'key.env')
load_dotenv(dotenv_path)

OPEN_AI_KEY = os.environ.get('OPENAI_API_KEY')