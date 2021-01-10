import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyAPI:

    def __init__(self):
        scope = "user-library-read user-top-read user-read-private"
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    def get_user_tracks(self):
        results = self.sp.current_user_saved_tracks()
        for idx, item in enumerate(results['items']):
            track = item['track']
            print(idx, track['artists'][0]['name'], " – ", track['name'])

    # def get_user_followers(self):
    #     result = self.sp.me()
    #     friends = result['followers']
    #     for idx, item in enumerate(friends['items']):
    #         track = item['track']
    #         print(idx, track['artists'][0]['name'], " – ", track['name'])    

    def get_user_top_tracks(self):
        results = self.sp.current_user_top_tracks()
        for idx, item in enumerate(results['items']):
            track = item['track']
            print(idx, track['artists'][0]['name'], " – ", track['name'])
        print("ran")

    def get_user_top_artists(self):
        results = self.sp.current_user_top_artists()
        print(results)
        for idx, item in enumerate(results['items']):
            artist = item['artist']
            print(idx, artist['name'])
        print("ran")

    

# spotify = SpotifyAPI()
# spotify.get_user_tracks()
# #spotify.get_user_followers()
# spotify.get_user_top_tracks()
# spotify.get_user_top_artists()

