from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/button")
def button():
    return render_template('index.html')


@app.route("/find_color")
def find_color():
    pass_in = request.args
    # if statements denoting what color was received by the click action
    if pass_in.get("key", "null") == 'red':
        color = 'tomato'
    elif pass_in.get("key", "null") == 'green':
        color = 'forestgreen'
    elif pass_in.get("key", "null") == 'blue':
        color = 'aqua'
    else:
        color = 'No color fit the parameter'
    return color
