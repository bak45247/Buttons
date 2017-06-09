from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/button")
def button():
    return render_template('index.html')


@app.route("/find_color")
def find_color():
    pass_in = request.args
    color_in = pass_in.get("buttonId", "null")
    # if statements denoting what color was received by the click action
    if color_in == 'red':
        color = 'tomato'
    elif color_in == 'green':
        color = 'forestgreen'
    elif color_in == 'blue':
        color = 'aqua'
    else:
        color = 'No color fit the parameter'
    return color
