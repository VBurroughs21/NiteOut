from flask import Flask, request, session, render_template, g, redirect, url_for, flash
import jinja2

app = Flask(__name__)

@app.route("/")
def index():
    """ Cover page: Start a new assessment, or continue where you left off."""
    return render_template("index.html")

@app.route("/assessment")
def assessment():
    """ Cycle through slides."""
    return render_template("assessment.html")

@app.route("/results")
def results():
    """ Present the results of the assessment."""
    return render_template("results.html")

