from flask import Blueprint, render_template, jsonify
#from app import db
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
profile = Blueprint('profile', __name__)

# engine = create_engine('mysql://root:rootroot@localhost/recommended_shorttv')
# metadata = MetaData(engine)

class RecommendedMovies(Base):
	
	__tablename__ = 'recommended_movies'
	__table_args__ = {'autoload':True}
   



def loadSession():
	""""""    
	#dbPath = 'places.sqlite'
	engine = create_engine('mysql://root:rootroot@localhost/recommended_shorttv')
 
	metadata = Base.metadata
	Session = sessionmaker(bind=engine)
	session = Session()
	return session
	#return session

session = loadSession()

# @profile.route("/sandeep")
# def hello_sandeep():
# 	return "This is my test flak app"

#print "this is db functions",dir(db)

tasks = [
	{
		'id': 1,
		'title': u'Buy groceries',
		'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
		'done': False
	},
	{
		'id': 2,
		'title': u'Learn Python',
		'description': u'Need to find a good Python tutorial on the web', 
		'done': False
	}
]

@profile.route('/todo/api/v1.0/user', methods=['GET'])
def get_movies():
	
	result = session.query(RecommendedMovies).limit(2).all()
	return jsonify({'movies': result})