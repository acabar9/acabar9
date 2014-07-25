from flask import render_template, Flask, request
from apps import app

from flaskext import wtf
from flaskext.wtf import Form, TextField, TextAreaField, SubmitField, validators, ValidationError

class ContactForm(Form):
	name = TextField("name", [validators.Required("Please enter your name.")])
	email = TextField("Email", [validators.Required("Please enter your email address."),validators.Email("Please enter valid email address.")])
	subject = TextField("Subject", [validators.Required("Please enter a subject.")])
	message = TextField("Message", [validators.Required("Please enter a message.")])
	submit = SubmitField("Send")

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = ContactForm()

	if request.method == 'POST' :
		if form.validate() == False :
			return render_template('index.html', form=form)
		else:
			return "Nice to meet you, " + form.name.data + " ! "

	return render_template('index.html', form=form)

