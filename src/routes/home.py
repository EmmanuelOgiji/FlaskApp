import json
import logging

import requests
from flask import render_template, request
from json2html import *

from data_objects.constants import log_level
from src.data_objects.playlist import Playlist
from utils.spotify import authenticate_spotify

logger = logging.getLogger()
logging.basicConfig(level=log_level)
logger.setLevel(log_level)


def user_form():
    logger.info("Rendering template")
    return render_template("user_home.html")


def get_track_artists(track):
    track_artists = []
    for artist in track.get("track").get("artists"):
        artist_name = artist.get("name")
        track_artists.append(artist_name)
    return track_artists


def get_playlist_tracks(user_id, playlist_dict):
    logger.info("Getting list of tracks in playlist")
    token = authenticate_spotify()
    playlist_id = playlist_dict.get("PlaylistId")

    response = (requests.get(
        url=f"https://api.spotify.com/v1/users/{user_id}/playlists/{playlist_id}/tracks",
        headers=dict(Authorization=f"Bearer {token}")
    )).json()
    logger.debug(f"Track list response: {response}")
    tracks = []
    for track in response.get("items"):
        track_name = track.get("track").get("name")
        track_artists = get_track_artists(track)
        tracks.append(dict(Song=track_name, Artists=track_artists))
    logger.debug(f"Track list: {tracks}")
    return tracks


def list_users_playlists():
    logger.info("Getting user's playlists")
    token = authenticate_spotify()
    user_id = request.form['user_id']

    response = (requests.get(
        url=f"https://api.spotify.com/v1/users/{user_id}/playlists",
        headers=dict(Authorization=f"Bearer {token}")
    )).json()
    logger.debug(f"Playlist response: {response}")
    playlists = []
    for playlist in response.get("items"):
        playlist_dict = Playlist(playlist).print_details()
        playlist_dict["Tracks"] = get_playlist_tracks(user_id, playlist_dict)
        playlists.append(playlist_dict)
    playlists_dict = dict(Playlists=playlists)
    logger.debug(f"Playlist dict: {response}")
    playlist_html = json2html.convert(json=json.dumps(playlists_dict))
    return playlist_html
