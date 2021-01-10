import spotipy
from spotipy.oauth2 import SpotifyOAuth
import re

class SpotifyAPI:

    def __init__(self):
        scope = "user-library-read user-top-read user-read-private"
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='7a44eed14f344b2285446586620d715b', client_secret='b8d7e61dc3194783993194d34b116c9b', redirect_uri='http://localhost/', scope=scope))

    def get_user_tracks(self):
        results = self.sp.current_user_saved_tracks()
        print(results)
        # for idx, item in enumerate(results['items']):
        #     track = item['uri']
            
        #     print(idx, track['artists'][0]['name'], " – ", track['name'])

    # def get_user_followers(self):
    #     result = self.sp.me()
    #     friends = result['followers']
    #     for idx, item in enumerate(friends['items']):
    #         track = item['track']
    #         print(idx, track['artists'][0]['name'], " – ", track['name'])    

    def get_user_top_tracks(self):
        results = self.sp.current_user_top_tracks()
        print(results)
        # for idx, item in enumerate(results['items']):
        #     track = item['track']
        #     print(idx, track['artists'][0]['name'], " – ", track['name'])
        # print("ran")

    def get_user_top_artists(self):
        results = self.sp.current_user_top_artists()
        print(results)
    def get_user_from_playlist_url(self, url):
        txt = re.search('t/.*\?', url).group(0)
        spotify_id = txt[2:-1]
        print(self.sp.playlist(spotify_id))

    def get_song_recs(self, artist_list, genre_list, track_list):
        artist_uris = [artist['uri'] for artist in artist_list]
        track_uris = [track['uri'] for track in track_list]
        genre_uris = [genre['uri'] for genre in genre_list]
        self.sp.recommendations(seed_artists=artist_uris, seed_tracks=track_uris, seed_genres=genre_uris, limit=5)

    def create_common_playlist(self, second_user, artist_list, genre_list, track_list):
        title = self.sp.me()['display_name'] + ' X ' + second_user
        artist_uris = [artist['uri'] for artist in artist_list]
        track_uris = [track['uri'] for track in track_list]
        genre_uris = [genre['uri'] for genre in genre_list]
        song_recs = self.sp.recommendations(seed_artists=artist_uris, seed_tracks=track_uris, seed_genres=genre_uris, limit=5)
        
        playlist = self.sp.user_playlist_create(self.sp.me()['id'], title)
        print("playlist:", playlist['uri'])
        items = [song['uri'] for song in song_recs['tracks']]
        self.sp.playlist_add_items(playlist['uri'], items)
# , {'name': 'Ras Fraser Jr.', 'uri': '1D2oK3cJRq97OXDzu77BFR'}, {'name': 'Maroon 5', 'uri': '04gDigrS5kc9YWfZHwBETP'}, {'name': 'BTS', 'uri': '3Nrfpe0tUJi4K4DXYWgMUX'}
# , {'name': 'This Love', 'uri':'6ECp64rv50XVz93WvxXMGF'}, {'name':'Supergirl - Radio Edit', 'uri':'0Mn61Ji3tvs6GCCGGcKepJ'}, {'name':'Let Me Be' , 'uri':'785bMwdG6YNiy9jXBiWKCQ'}
# NOT MORE THAN 5 SEEDS in total
# shared_artists = [{'name': 'Icona Pop', 'uri': '1VBflYyxBhnDc9uVib98rw'}, {'name': 'Ras Fraser Jr.', 'uri': '1D2oK3cJRq97OXDzu77BFR'}]
# shared_songs = [{'name': 'Dynamite', 'uri': '0t1kP63rueHleOhQkYSXFY'}, {'name':'Let Me Be', 'uri':'3rZlBLELWMxRS3R1OaE3D8'}]
# shared_genres = [] 
# spotify = SpotifyAPI()
# spotify.get_song_recs(shared_artists, shared_genres, shared_songs)
# spotify.create_common_playlist('Brian', shared_artists, shared_genres, shared_songs)
# spotify.get_user_tracks()
# #spotify.get_user_followers()
# spotify.get_user_top_tracks()
# spotify.get_user_top_artists()
# spotify.get_user_from_playlist_url('https://open.spotify.com/playlist/37i9dQZF1DWV4UmHQGouUW?si=WDGgYXO3Q7a2STBs5qOnBQ')


