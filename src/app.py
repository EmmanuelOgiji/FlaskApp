"""
As a user of this app,
when I enter the name of a spotify playlist
and click submit
then
"""
import base64
import json

import requests
from flask import Flask, render_template, request

from src.data_objects.playlist import Playlist

app = Flask(__name__)

clientId = "b5e1ecfbd8fc43d49129ae96eafce387"
clientSecret = "c142e97219c94c5991d0e8ff1031c0ee"


@app.route('/')
def user_form():
    return render_template("user_home.html")


def encode_to_base64(message):
    messagebytes = message.encode('ascii')
    base64bytes = base64.b64encode(messagebytes)
    base64message = base64bytes.decode('ascii')
    return base64message


def authenticate_spotify():
    message = encode_to_base64(f"{clientId}:{clientSecret}")
    response = requests.post(
        url="https://accounts.spotify.com/api/token",
        headers=dict(
            Authorization=f"Basic {message}"
        ),
        data=dict(grant_type="client_credentials")

    )

    token = response.json()['access_token']
    return token


@app.route('/', methods=['POST'])
def list_users_playlists():
    token = authenticate_spotify()
    user_id = request.form['user_id']

    response = (requests.get(
        url=f"https://api.spotify.com/v1/users/{user_id}/playlists",
        headers=dict(Authorization=f"Bearer {token}")
    )).json()
    playlists = []
    for playlist in response.get("items"):
        playlists.append(Playlist(playlist).print_details())
    return json.dumps(playlists)


if __name__ == '__main__':
    app.run()
