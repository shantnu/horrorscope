from flask import Flask, redirect, render_template, \
     request, url_for, jsonify
import random



app = Flask(__name__)


@app.route("/")
def hello_from_root():
    return render_template(
        'mvp2.html')

@app.route("/yo")
def yo():
    data = "hello random the rain in spain falls mainly on the plain" + str(random.randrange(1, 1000))
    return jsonify({"result": data })


@app.route("/hello")
def hello():
    return jsonify(message='Hello from path!')


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)


app.run(debug=True)