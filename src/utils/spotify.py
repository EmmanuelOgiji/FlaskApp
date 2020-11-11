import logging

import requests

from src.data_objects.constants import CLIENT_ID, CLIENT_SECRET, log_level
from src.utils.generic import encode_to_base64

logger = logging.getLogger()
logging.basicConfig(level=log_level)
logger.setLevel(log_level)


def authenticate_spotify():
    logger.info("Getting Access Token from Spotify")
    message = encode_to_base64(f"{CLIENT_ID}:{CLIENT_SECRET}")
    response = requests.post(
        url="https://accounts.spotify.com/api/token",
        headers=dict(
            Authorization=f"Basic {message}"
        ),
        data=dict(grant_type="client_credentials")

    )

    token = response.json()['access_token']
    logger.debug(f"Token: {token}")
    return token
