# Autotrader
import os

import hug
from dotenv import load_dotenv

from autotrader import app

load_dotenv()


@hug.extend_api()
def init_app():
    return [app]

