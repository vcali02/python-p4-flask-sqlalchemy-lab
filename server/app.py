#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

#Each view should display all attributes as line items (ul). 
#If there is a one-to-many relationship, 
#each of the many should have its own line item.




@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    #if the Animal.id is equal to the ID IN THE PARAMETER....
    animal = Animal.query.filter(Animal.id == id).first()
    #declare variable for what will be the BODY OF YOUR RESPONSE
    #declare it to an "interpolable" empty string
    response_body = f''
    #ADD the interpolated string to the empty string from above
    response_body += f'<ul>ID: {animal.id}</ul>'
    response_body += f'<ul>Name: {animal.name}</ul>'
    response_body += f'<ul>Species: {animal.species}</ul>'
    response_body += f'<ul>Zookeeper: {animal.zookeeper.name}</ul>'
    response_body += f'<ul>Enclosure: {animal.enclosure.environment}</ul>'
    #use make_response method
    return make_response(response_body)

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()
    response_body = f''
    response_body += f'<ul>ID: {zookeeper.id}</ul>'
    response_body += f'<ul>Name: {zookeeper.name}</ul>'
    response_body += f'<ul>Birthday: {zookeeper.birthday}</ul>'

    #WHY A LOOP?
    #for every animal in the zookeeper table under the animals attribute
    for animal in zookeeper.animals:
    #grab the empty interpolable string that will makeup the response body
    #and add the interpolated string
    #that interpolated string will be grabbing the animals attribute, 
    #specifically the name associated with it
        response_body += f'<ul>Animals: {animal.name}</ul>'

    return make_response(response_body)

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()
    response_body = f''
    response_body += f'<ul>ID: {enclosure.id}</ul>'
    response_body += f'<ul>Environment: {enclosure.environment}</ul>'
    response_body += f'<ul>Open to Visitors: {enclosure.open_to_visitors}</ul>'

    for animal in enclosure.animals:
        response_body += f'<ul>Animals: {animal.name}</ul>'
    return make_response(response_body)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
