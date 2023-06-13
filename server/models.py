from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

#The Zookeeper model should contain:
# a name, a birthday, and a list of animals that they take care of.
class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)
    birthday = db.Column(db.String)
    #animals = db.Column(db.String)

    #RELATIONSHIP
    #Zookeeper class animalse attribute is accessed through the Animal class zookeeper attribute
    animals = db.relationship('Animal', back_populates= 'zookeeper')



#The Enclosure model should contain:
# an environment (grass, sand, or water), an open_to_visitors boolean, and a list of animals
class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)

    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)
    #animals = db.Column(db.String)

    #RELATIONSHIP
    #Enclosure class animals attribute is accessed through the Animal class enclosure attribute
    animals = db.relationship('Animal', back_populates= 'enclosure')



#The Animal model should contain:
# a name, a species, a zookeeper, and an enclosure.
class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)
    species = db.Column(db.String)
    #zookeeper = db.Column(db.String)
    #enclosure = db.Column(db.String)

    #FOREIGN KEY
    # variable name   make a column (contains int)  make foreign key and pass param table_name.id
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))

    #RELATIONSHIP
    #Animal class zookeeper attribute is accessed through the Zookeeper class animals_in_care attribute
    zookeeper = db.relationship('Zookeeper', back_populates= 'animals')
    #Animal class enclosure attribute is accessed through the Enclosure class animals_list attribute
    enclosure = db.relationship('Enclosure', back_populates= 'animals')
