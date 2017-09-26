import os
import sys
import configparser


from flask import Blueprint, render_template, jsonify
from flask import Flask, flash, redirect, render_template, request, session, abort
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



config = configparser.ConfigParser()
config.readfp(open(r'config.txt'))

rating_file = config.get('FILE-CONFIG', 'rating_file')
movie_file = config.get('FILE-CONFIG', 'movie_file')
user_file = config.get('FILE-CONFIG', 'user_file')


##Db info
HOST = config.get('DB-PRODUCTION', 'HOST')
USER = config.get('DB-PRODUCTION', 'USER')
PASSWD = config.get('DB-PRODUCTION', 'PASSWD')
DB = config.get('DB-PRODUCTION', 'DB')



#from app import db
 



profile = Blueprint('profile', __name__)

# engine = create_engine('mysql://root:rootroot@localhost/recommended_shorttv')
# metadata = MetaData(engine)
engine = create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.format(USER, PASSWD, HOST, DB))

Base = declarative_base()
Base.metadata.bind = engine



class RecommendedMovies(Base):
	
	__tablename__ = 'recommended_movies'
	__table_args__ = {'autoload':True}
   



def loadSession():
	""""""    
	#dbPath = 'places.sqlite'
	
 
	metadata = Base.metadata
	Session = sessionmaker(bind=engine)
	db_session = Session()
	return db_session
	#return session

db_session = loadSession()

# @profile.route("/sandeep")
# def hello_sandeep():
# 	return "This is my test flak app"

#print "this is db functions",dir(db)


@profile.route('/todo/api/v1.0/recommended_movies', methods=['GET'])
def get_recommended_movies_to_users():
	user_dict={}
	result = db_session.query(RecommendedMovies).all()
	for i in result:
		user_dict.update({i.user_id:i.movies})
	return user_dict


@profile.route('/todo/api/v1.0/user/<int:user_id>', methods=['GET'])
def get_recommended_movies_to_specific_user(user_id = None):
	user_dict={}
	if user_id:
		result = db_session.query(RecommendedMovies).filter(RecommendedMovies.user_id == user_id).all()
		for i in result:
			user_dict.update({i.user_id:i.movies})
	return user_dict


@profile.route('/')
def home():
	
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return "Hello Boss!"


@profile.route('/login', methods=['POST'])
def do_admin_login():
	if request.form['password'] == 'password' and request.form['username'] == 'admin':
		session['logged_in'] = True
	else:
		return render_template('index.html')