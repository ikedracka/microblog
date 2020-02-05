from flask import render_template
from app import app
#decorators
# A decorator modifies the function that follows it.
@app.route('/')
@app.route('/index')
def index():
    user={'name':'Ilona'}
    # fake objects - placeholder as we don't have connection to other datasource
    posts = [
        {
            'author': {'username': 'John'},
            'message': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'message': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Ilona', user=user, posts=posts)