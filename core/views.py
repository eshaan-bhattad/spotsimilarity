from django.shortcuts import render, redirect
from django.http import HttpResponse
from .spotify import SpotifyAPI
from . import graphs, message
import plotly.graph_objects as go
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Create your views here.

def index(request):
	testing = "Profiled Playlist"
	if request.GET.get('watchlist') is not None:
		spotify = SpotifyAPI()
		user_list, user_artist_list = spotify.get_user_top_tracks()
		user_list_2, user_artist_list_2 = spotify.get_user_tracks()
		user_list = user_list + user_list_2
		user_artist_list_2 = user_artist_list + user_artist_list_2
		friend_list, friend_artist_list = spotify.get_playlist_songs('https://open.spotify.com/playlist/37i9dQZF1DWV4UmHQGouUW?si=WDGgYXO3Q7a2STBs5qOnBQ')
		shared_list = list(set(user_list).union(set(friend_list)))
		shared_artist_list = list(set(user_artist_list).union(set(friend_artist_list)))
		print("___________Here's your shared artists___________")
		for i in shared_artist_list:
			print(spotify.get_artist(i)['name'])
		print("___________Here's your shared songs___________")
		for i in shared_list:
			print(spotify.get_song(i)['name'])
		if len(shared_artist_list) > 3:
			shared_artist_list = shared_artist_list[0:3]
		if len(shared_list) > 3:
			shared_list = shared_list[0:3]
		
		#spotify.get_song_recs(shared_artist_list, ['pop'], [shared_list[0]])
		#spotify.get_song_recs([shared_artist_list[0]], ['pop'], shared_list)
		#user_id = spotify.get_user_from_playlist_url('https://open.spotify.com/playlist/37i9dQZF1DWV4UmHQGouUW?si=WDGgYXO3Q7a2STBs5qOnBQ')
		url = spotify.create_common_playlist("Eshaan", shared_artist_list, ['pop'], shared_list)
		
		report = message.message(compatability, 11, 5, 10, 2, 15, 5, 23, 12, 40, 40)
		
		return render(request, 'comparison.html', {
		'testing' : testing,
		'bar_graph' : bar_graph,
		'partner' : partner,
		'compatability' : compatability,
		'playlist_url': url,
		'report' : report,
		})
	
	return render(request, 'index.html', {
		'testing' : testing,
		})

def about(request):
	testing = "Profiled Playlist"
	return render(request, 'about.html', {
		'testing' : testing,
		})

def comparison(request):
	testing = "Profiled Playlist"
	graph_data = 20, 14, 23, 5, 34
	bar_graph = graphs.graph(20, 14, 23, 5, 34)

	partner = "John Smith"
	compatability = 55

	report = message.message(compatability, 11, 5, 10, 2, 15, 5, 23, 12, 40, 40)

	return render(request, 'comparison.html', {
		'testing' : testing,
		'bar_graph' : bar_graph,
		'partner' : partner,
		'compatability' : compatability,
		'report' : report,
		})
