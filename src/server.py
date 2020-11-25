from gevent.pywsgi import WSGIServer

import src.routes.task
import src.routes.trello_crawler
import src.routes.user
from src.config.config import Config
from src.api import zac


config = Config()
port = config.get_zac_port()

http_server = WSGIServer(("", port), zac)
