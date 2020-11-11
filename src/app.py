"""
As a user of this app,
when I enter my user id
and click submit
then I get details of all my playlists
"""
import logging

from flask import Flask

from data_objects.constants import log_level
from routes.home import user_form, list_users_playlists

logger = logging.getLogger()
logging.basicConfig(level=log_level)
logger.setLevel(log_level)

app = Flask(__name__)


@app.route('/')
def home_page():
    logger.info("Opening form home page")
    return user_form()


@app.route('/', methods=['POST'])
def home_post():
    logger.info("Posting form result")
    return list_users_playlists()


if __name__ == '__main__':
    app.run()
