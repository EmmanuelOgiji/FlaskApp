"""
As a user of this app,
when I enter the name of a spotify playlist
and click submit
then
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text


if __name__ == '__main__':
    app.run()
