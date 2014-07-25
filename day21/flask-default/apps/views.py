from flask import render_template, Flask
from apps import app


@app.route('/')
@app.route('/index')
def index():
	age=21
	species="lion"
	friend=["google","teacher","student"]

	return render_template("index.html", age=age,\
		species=species,friend=friend)