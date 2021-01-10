from django.shortcuts import render
from django.http import HttpResponse
from .spotify import SpotifyAPI
from . import graphs
import plotly.graph_objects as go

# Create your views here.

def index(request):
	testing = "Profiled Playlist"
	if request.GET.get('watchlist') is not None:
		spotify = SpotifyAPI()
		# spotify.get_user_tracks()
		# spotify.get_user_top_tracks()
		# spotify.get_user_top_artists()
	
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
	compatability = 25

	return render(request, 'comparison.html', {
		'testing' : testing,
		'bar_graph' : bar_graph,
		'partner' : partner,
		'compatability' : compatability,
		})
