from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_index():
    return render_template('index.html')


@app.route('/departures/<departure>/')
def render_departure():
    return render_template('departure.html')


@app.route('/tours/<id>')
def render_tour():
    return render_template('tour.html')


app.run()