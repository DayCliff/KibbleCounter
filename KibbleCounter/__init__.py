from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='static')
@app.route('/')
def main():
    return render_template("base.html")
@app.route('/calculate', methods=['POST'])
def calculate():
    x = request.form['x']
    y = request.form['y']
    z = request.form['z']

    cups_per_bag = (float(x) * float(y))/float(z)

    return render_template('base.html', result=cups_per_bag)
