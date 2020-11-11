import requests

from src.data_objects.constants import CLIENT_ID, CLIENT_SECRET
from src.utils.generic import encode_to_base64


def authenticate_spotify():
    message = encode_to_base64(f"{CLIENT_ID}:{CLIENT_SECRET}")
    response = requests.post(
        url="https://accounts.spotify.com/api/token",
        headers=dict(
            Authorization=f"Basic {message}"
        ),
        data=dict(grant_type="client_credentials")

    )

    token = response.json()['access_token']
    return token
