import plotly.graph_objects as go

def graph(tracks, artists, explicit, duration, popularity):
	x = ['Common Tracks', 'Common Artists', 'Num of Explicit Songs', 'Avg Duration', 'Popularity']
	y = [tracks, artists, explicit, duration, popularity]

	# Use the hovertext kw argument for hover text
	fig = go.Figure(data=[go.Bar(x=x, y=y,)])
	# Customize aspect
	fig.update_traces(marker_color='rgb(30,215,96)', marker_line_color='rgb(25,25,20)',
	                  marker_line_width=3, opacity=1)
	# fig.show()
	plot_html = fig.to_html(full_html=False, include_plotlyjs=False)

	return plot_html

# graph(20, 14, 23, 5, 34)