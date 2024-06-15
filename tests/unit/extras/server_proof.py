#!/usr/bin/python3
from datetime import timedelta
from flask import Flask, request, jsonify, render_template, Response, session, send_from_directory, abort
from flask.helpers import flash, url_for
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = "27eduCBA09"


@app.before_request
def make_session_permanent():
	# Para renovar la sesión cada 60 minutos
	session.permanent = False
	app.permanent_session_lifetime = timedelta(minutes=60)


@app.route('/simple_get', methods=['GET'])
def simple_get():
	return 'Hello, World!'


@app.route('/params_get', methods=['GET'])
def params_get():
	args = request.args
	return args


@app.route('/simple_post', methods=['POST'])
def simple_post():
	return request.form['hola'], 200


@app.route('/file_post', methods=['POST'])
def file_post():
	return jsonify(request.form), 200


@app.route('/simple_redirect', methods=['GET'])
def simple_redirect():
	return redirect("/simple_get")


@app.route('/double_get', methods=['GET'])
def double_get():
	return redirect(url_for('simple_redirect'))


@app.route('/headers', methods=['GET'])
def headers_get():
	return request.headers['User-Agent']


@app.route('/showcookie')
def getcookie():
	name = request.cookies
	return name


if __name__ == '__main__':
	app.run(debug=True)
