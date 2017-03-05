import os
from os.path import join, dirname, abspath
import importlib

from dotenv import load_dotenv


# Load environment variables
# ENV_PATH = join(abspath(dirname(dirname(__file__))), '.env')
ENV_PATH = os.getcwd()
load_dotenv(join(ENV_PATH, '.env'))

# import all settings
settings = importlib.import_module(os.getenv('TORNADO_SETTINGS_MODULE'))
