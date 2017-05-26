from flask import Flask, request, redirect
import logging, inspect
from flask import render_template, render_template_string

# configuration
DEBUG = False
SECRET_KEY = 'development key'


app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def noinj():
    try:
        return render_template('index.html')
    except Exception as e:
        logging.exception('Exception: FUNCTION: '+inspect.stack()[0][3]+'('+inspect.stack()[1][3]+')')
        return '{}'

@app.errorhandler(404)
def page_not_found(e):
    template = '''<html><body>
    <div class="center-content error">
        <h1>Oops! That page doesn't exist.</h1>
        <h3>%s</h3>
    </div>
</body></html>
''' % (request.url)
    return render_template_string(template), 404
