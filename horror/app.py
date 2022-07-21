from flask import Flask, redirect, render_template, \
     request, url_for, jsonify
import random
from horror import horror_list
from flask_s3 import FlaskS3

app = Flask(__name__)
app.config['FLASKS3_BUCKET_NAME'] = 'docker-on-aws-shantnu'
s3 = FlaskS3(app)

@app.route("/")
def hello_from_root():
    return render_template(
        'mvp2.html')

@app.route("/yo")
def yo():
    data = random.choice(horror_list)
    return jsonify({"result": data })


@app.route("/hello")
def hello():
    return jsonify(message='Hello from path!')


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)


#app.run(debug=True)