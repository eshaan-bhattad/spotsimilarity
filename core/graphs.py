import plotly.graph_objects as go

def graph(tracks, artists, explicit, duration, popularity):
	x = ['Common Tracks', 'Common Artists', 'Num of Explicit Songs', 'Avg Duration', 'Popularity']
	y = [tracks, artists, explicit, duration, popularity]

	# Use the hovertext kw argument for hover text
	fig = go.Figure(data=[go.Bar(x=x, y=y,)])
	# Customize aspect
	fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
	                  marker_line_width=1.5, opacity=0.6)
	fig.show()

# graph(20, 14, 23, 5, 34)