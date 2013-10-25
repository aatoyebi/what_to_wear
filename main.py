import flask, flask.views
import os
import urllib
import re
from xml.dom import minidom
from pprint import pprint

WEATHER_URL = 'http://xml.weather.yahoo.com/forecastrss?p=%s'
WEATHER_NS = 'http://xml.weather.yahoo.com/ns/rss/1.0'

class Main(flask.views.MethodView):
    def get(self, page='index'):
        page += '.html'

        if os.path.isfile('templates/' + page):
            return flask.render_template(page)
        flask.abort(404)
        

    def post(self):
        zip_code = flask.request.form['zipcode']
        regex = re.compile(r"[^0-9]")
        if len(flask.request.form['zipcode']) != 5:
            if len(flask.request.form['zipcode']) == 0:
                flask.flash("Please enter zipcode.")
            elif len(flask.request.form['zipcode']) < 5:
                flask.flash("Oops, you're a few digits behind. Please re-enter zipcode.") 
            if len(flask.request.form['zipcode']) > 5:
                flask.flash("Oops, you're a few digits ahead. Please re-enter zipcode.")        
            return flask.redirect(flask.url_for('main'))

        elif int(zip_code):  
            url = WEATHER_URL % zip_code
            dom = minidom.parse(urllib.urlopen(url))
            forecasts = []
            location = []
            suggestions = {
            "warm_rain": "It's warm. But you should take an umbrella along.",
            "wind": "Put on a wind breaker.",
            "hot": "Looks like a flip flops and sunglasses type of weather. Don't forget the sunscreen!",
            "rain": "You should take an umbrella along.",
            "snow": "Wear your winter jacket and take an umbrella along.",
            "mild": "Don't forget to grab a light jacket or hoodie.",
            "chilly": "Maybe you should put on a sweater...and pants.",
            "cold": "Grab your coat. No, not the heavy one.",
            "very_cold": "It's cold outside. Don't forget your coat and thermal underwear!",
            "freezing": "Brrr...do you really need to go outside? You do? Fine, layer up like crazy and put on your heaviest coat."
            }
            for node in dom.getElementsByTagNameNS(WEATHER_NS, 'forecast'):
                forecasts.append({
                    str('date'): str(node.getAttribute('date')),
                    str('low'): int(node.getAttribute('low')),
                    str('high'): int(node.getAttribute('high')),
                    str('condition'): str(node.getAttribute('text'))
                })

            for node in dom.getElementsByTagNameNS(WEATHER_NS, 'location'):
                location.append({
                    'city': str(node.getAttribute('city')), 
                    'region': str(node.getAttribute('region'))
                })

            ycondition = dom.getElementsByTagNameNS(WEATHER_NS, 'condition')[0]

            for i in range(len(forecasts)):
                if forecasts[i]['high'] >= 75:
                    if "Thunderstorms" in forecasts[i]['condition'] or "Showers" in forecasts[i]['condition'] or "Rain" in forecasts[i]['condition'] or "Storm" in forecasts[i]['condition'] or "Hail" in forecasts[i]['condition'] or "Drizzle" in forecasts[i]['condition']:
                        flask.flash(suggestions["warm_rain"])
                        return flask.render_template('rainy.html')
                    elif "Fog" in forecasts[i]['condition'] or "Haze" in forecasts[i]['condition'] or "Windy" in forecasts[i]['condition']:
                        flask.flash(suggestions["wind"])  
                        return flask.render_template('haze.html')  
                    else:    
                        flask.flash(suggestions["hot"])
                        return flask.render_template('warm.html')


                elif forecasts[i]['high'] < 75 and forecasts[i]['high'] >= 65:
                    if "Thunderstorms" in forecasts[i]['condition'] or "Showers" in forecasts[i]['condition'] or "Rain" in forecasts[i]['condition'] or "Storm" in forecasts[i]['condition'] or "Hail" in forecasts[i]['condition'] or "Drizzle" in forecasts[i]['condition']:
                        flask.flash(suggestions["rain"])
                        return flask.render_template('rainy.html')
                    elif "Snow" in forecasts[i]['condition'] or "Sleet" in forecasts[i]['condition']:
                        flask.flash(suggestions["snow"])  
                        return flask.render_template('snowy.html') 
                    elif "Fog" in forecasts[i]['condition'] or "Haze" in forecasts[i]['condition'] or "Windy" in forecasts[i]['condition']:
                        flask.flash(suggestions["wind"]) 
                        return flask.render_template('haze.html')      
                    else:    
                        flask.flash(suggestions["mild"])
                        return flask.render_template('music.html')

                elif forecasts[i]['high'] < 65 and forecasts[i]['high'] >= 55:
                    if "Thunderstorms" in forecasts[i]['condition'] or "Showers" in forecasts[i]['condition'] or "Rain" in forecasts[i]['condition'] or "Storm" in forecasts[i]['condition'] or "Hail" in forecasts[i]['condition'] or "Drizzle" in forecasts[i]['condition']:
                        flask.flash(suggestions["rain"])
                        return flask.render_template('rainy.html')
                    elif "Snow" in forecasts[i]['condition'] or "Sleet" in forecasts[i]['condition']:
                        flask.flash(suggestions["snow"])   
                        return flask.render_template('snowy.html')
                    elif "Fog" in forecasts[i]['condition'] or "Haze" in forecasts[i]['condition'] or "Windy" in forecasts[i]['condition']:
                        flask.flash(suggestions["wind"])  
                        return flask.render_template('haze.html')     
                    else:    
                        flask.flash(suggestions["chilly"])
                        return flask.render_template('music.html')

                elif forecasts[i]['high'] < 55 and forecasts[i]['high'] >= 45:
                    if "Thunderstorms" in forecasts[i]['condition'] or "Showers" in forecasts[i]['condition'] or "Rain" in forecasts[i]['condition'] or "Storm" in forecasts[i]['condition'] or "Hail" in forecasts[i]['condition'] or "Drizzle" in forecasts[i]['condition']:
                        flask.flash(suggestions["rain"])
                        return flask.render_template('rainy.html')
                    elif "Snow" in forecasts[i]['condition'] or "Sleet" in forecasts[i]['condition']:
                        flask.flash(suggestions["snow"]) 
                        return flask.render_template('snowy.html') 
                    elif "Fog" in forecasts[i]['condition'] or "Haze" in forecasts[i]['condition'] or "Windy" in forecasts[i]['condition']:
                        flask.flash(suggestions["wind"])    
                        return flask.render_template('haze.html')    
                    else:    
                        flask.flash(suggestions["cold"])
                        return flask.render_template('music.html')

                elif forecasts[i]['high'] < 45 and forecasts[i]['high'] >= 35:
                    if "Thunderstorms" in forecasts[i]['condition'] or "Showers" in forecasts[i]['condition'] or "Rain" in forecasts[i]['condition'] or "Storm" in forecasts[i]['condition'] or "Hail" in forecasts[i]['condition'] or "Drizzle" in forecasts[i]['condition']:
                        flask.flash(suggestions["rain"])
                        return flask.render_template('rainy.html')
                    elif "Snow" in forecasts[i]['condition'] or "Sleet" in forecasts[i]['condition']:
                        flask.flash(suggestions["snow"])  
                        return flask.render_template('snowy.html')
                    elif "Fog" in forecasts[i]['condition'] or "Haze" in forecasts[i]['condition'] or "Windy" in forecasts[i]['condition']:
                        flask.flash(suggestions["wind"])  
                        return flask.render_template('haze.html')      
                    else:    
                        flask.flash(suggestions["very_cold"]) 
                        return flask.render_template('music.html')

                elif forecasts[i]['high'] < 35:
                    if "Thunderstorms" in forecasts[i]['condition'] or "Showers" in forecasts[i]['condition'] or "Rain" in forecasts[i]['condition'] or "Storm" in forecasts[i]['condition'] or "Hail" in forecasts[i]['condition'] or "Drizzle" in forecasts[i]['condition']:
                        flask.flash(suggestions["rain"])
                        return flask.render_template('rainy.html')
                    elif "Snow" in forecasts[i]['condition'] or "Sleet" in forecasts[i]['condition']:
                        flask.flash(suggestions["snow"])   
                        return flask.render_template('snowy.html')
                    elif "Fog" in forecasts[i]['condition'] or "Haze" in forecasts[i]['condition'] or "Windy" in forecasts[i]['condition']:
                        flask.flash(suggestions["wind"]) 
                        return flask.render_template('haze.html')      
                    else:    
                        flask.flash(suggestions["freezing"])  
                        return flask.render_template('music.html')     

                return flask.redirect(flask.url_for('main'))
        else:
            flask.flash("Please enter a valid zipcode.")
            return flask.redirect(flask.url_for('main'))     

        
        
        

    
