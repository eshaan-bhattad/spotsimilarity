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
		# spotify.get_user_tracks()
		# spotify.get_user_tracks()
		# spotify.get_song_recs([{'name': 'Icona Pop', 'uri': '1VBflYyxBhnDc9uVib98rw'}, {'name': 'Ras Fraser Jr.', 'uri': '1D2oK3cJRq97OXDzu77BFR'}], [], [{'name': 'Dynamite', 'uri': '0t1kP63rueHleOhQkYSXFY'}, {'name':'Let Me Be', 'uri':'3rZlBLELWMxRS3R1OaE3D8'}])
		# spotify.get_user_from_playlist_url('https://open.spotify.com/playlist/37i9dQZF1DWV4UmHQGouUW?si=WDGgYXO3Q7a2STBs5qOnBQ')
		spotify.get_user_top_tracks()
		return redirect('/comparison')
	
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
