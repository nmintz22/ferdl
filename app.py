from flask import Flask, render_template, request, url_for
import random

application = Flask(__name__,
                    static_url_path='/static')

@application.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    application.run(debug=True)