from gevent.pywsgi import WSGIServer

import src.routes.task
import src.routes.trello_crawler
from src.config.config import Config
from src.api import zac


config = Config()
host = config.get_zac_host()
port = config.get_zac_port()

http_server = WSGIServer((host, port), zac)
