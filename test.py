import datetime

import requests
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    year = datetime.date.today().year
    return render_template("test.html", year=year)


@app.route('/project/<id>')
def display_project(id):
    year = datetime.date.today().year
    response = requests.get(url="https://api.npoint.io/b64ff1d4b6dae1e6d6ec")
    projects = response.json()
    for project in projects:
        if project['id'] == int(id):
            return render_template("project.html", year=year, project=project)


if __name__ == "__main__":
    app.run()
