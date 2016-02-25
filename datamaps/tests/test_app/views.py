from flask import render_template
from test_app import app


@app.route('/')
def test_all_map_elems():
    return render_template('test_all_map_elems.html')

@app.route('/default_map_options/')
def test_default_map_options():
    return render_template('test_color_change.html')