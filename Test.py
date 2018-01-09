from flask import Flask, render_template

import process

app = Flask(__name__)

@app.route('/rewards')
def rewards():
    return render_template('rewards.html')

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/layout1')
def layout1():
    return render_template('layout1.html')

@app.route('/posb')
def posb():
    t = []
    t = process.processTransaction()
    return render_template('posb.html',zz = t)

@app.route('/TomTH')
def transactionhistory():
    return render_template('TomTH.html')

if __name__ == '__main__':
    app.run()
