import logging
import os
from dataclasses import dataclass
import sys


from dotenv import load_dotenv

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO, stream=sys.stdout)
#logging.basicConfig(level=logging.INFO, stream=sys.stdout)
load_dotenv()


@dataclass
class Settings:
    try:
        #BOT_TOKEN: str = os.environ.get('BOT_TOKEN')
        BOT_TOKEN = os.environ["BOT_TOKEN"]
        BOT_NAME = os.environ["BOT_NAME"]
        BOT_USERNAME = os.environ["BOT_USERNAME"]
    except KeyError as err:
        logging.critical(f" Can't read {err} from enviroment variables.")
        raise KeyError(err)
  

settings = Settings()