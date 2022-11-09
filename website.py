from flask import Flask, render_template
from connection import conn

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('interface.html', filepath=conn.pull_cat_image())