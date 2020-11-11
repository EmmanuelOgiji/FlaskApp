import json

import requests
from flask import render_template, request
from json2html import *

from src.data_objects.playlist import Playlist
from utils.spotify import authenticate_spotify


def user_form():
    return render_template("user_home.html")


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
    playlists_dict = dict(Playlists=playlists)
    return json2html.convert(json=json.dumps(playlists_dict))
