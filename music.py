import flask, flask.views
import os
import utils
from main import Main



class Music(flask.views.MethodView):
	def get(self):
		return flask.render_template('music.html')

	def post(self):	
		if "Thunderstorms" in main.forecasts['condition']:
			return flask.render_template('rainy.html')
		else:
			return flask.render_template('music.html')
				
		"""elif "Snow" in Main.forecasts[i]['condition'] or "Sleet" in Main.forecasts[i]['condition'] or "Cold" in Main.forecasts[i]['condition']:
			return flask.render_template('snowy.html')
		elif "Hot" in Main.forecasts[i]['condition'] or "Sunny" in Main.forecasts[i]['condition'] or "Warm" in Main.forecasts[i]['condition']:
			return flask.render_template('warm.html') 
		elif "Haze" in Main.forecasts[i]['condition'] or "Foggy" in Main.forecasts[i]['condition'] or "Smoky" in Main.forecasts[i]['condition'] or "Dust" in Main.forecasts[i]['condition']:
			return flask.render_template('haze.html')  
		return flask.render_template('music.html')	"""
				