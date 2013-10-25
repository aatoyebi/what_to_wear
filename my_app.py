import flask
import settings


#Views
from main import Main
from remote import Remote
from music import Music

app = flask.Flask(__name__)

app.secret_key = settings.secret_key

#Routes
main_view_func = Main.as_view('main')

app.add_url_rule('/',
             view_func=main_view_func,
             methods=["GET", "POST"])

@app.errorhandler(404)
def page_not_found(error):
	return flask.render_template('404.html'), 404

app.debug = True
app.run()