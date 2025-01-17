from models import Person
from flask import render_template

def register_routes(app, db):
    
    @app.route('/')
    def index():
        persons = Person.query.all()
        return render_template('index.html', persons=persons)