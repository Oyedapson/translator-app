from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from functools import wraps
import index 
import sys

app = Flask(__name__)


language = ''

@app.route('/', methods=['GET','POST'])
def main():
    if request.method == 'POST':
        session['language'] = request.form['language']
        return render_template('home.html',languages = index.showLanguages(), flag="block", text="")
    return render_template('home.html',languages = index.showLanguages(), flag="none", text="")

@app.route('/recognise', methods=['GET','POST'])
def speak():
    language = session['language']
    input = index.speak()
    print(input)
    if input == "":
        return render_template('home.html',languages = index.showLanguages(), flag="block", text="try again")
    return render_template('home.html',languages = index.showLanguages(), flag="none", text=index.convert(input, language))
    if request.method == 'POST':
        session['language'] = request.form['language']
        return render_template('home.html',languages = index.showLanguages(), flag="block", text="")

if __name__ == '__main__':
    app.secret_key="secret123"
    app.run(debug=True)
