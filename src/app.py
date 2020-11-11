"""
As a user of this app,
when I enter my user id
and click submit
then I get details of all my playlists
"""
from flask import Flask

from routes.home import user_form, list_users_playlists

app = Flask(__name__)


@app.route('/')
def home_page():
    return user_form()


@app.route('/', methods=['POST'])
def home_post():
    return list_users_playlists()


if __name__ == '__main__':
    app.run()
