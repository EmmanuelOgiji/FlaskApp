class Playlist:
    def __init__(self, playlist_dict):
        self.name = playlist_dict.get("name")
        self.id = playlist_dict.get("id")
        self.track_details = playlist_dict.get("tracks")

    def print_details(self):
        return dict(
            PlaylistName=self.name,
            PlaylistId=self.id,
            TrackCount=self.track_details.get("total")
        )
