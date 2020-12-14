from flask import Flask, render_template
from data import title, departures, tours

app = Flask(__name__)


@app.route('/')
def render_index():
    return render_template('index.html')


@app.route('/data/')
def render_data():
    return render_template('data.html',
                           title=title,
                           tours=tours)


@app.route('/data/departures/<departure>/')
def render_data_depature(departure):
    return render_template('data_depature.html',
                           title=title,
                           tours=tours,
                           departure=departure,
                           departures=departures)


@app.route('/data/tours/<int:id>/')
def render_data_tour(id):
    return render_template('data_tours.html',
                           title=title,
                           id=id,
                           tours=tours,
                           departures=departures)


@app.route('/departures/<departure>/')
def render_departure():
    return render_template('departure.html')


@app.route('/tours/<id>')
def render_tour():
    return render_template('tour.html')


app.run()
