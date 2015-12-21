from flask import Flask, request, render_template, url_for
from models import select_college_holder
import os
from search import search
from pymongo import MongoClient

connection = MongoClient()
#colleges = connection.colleges_holder.colleges.find()



app = Flask(__name__)

@app.route("/index", methods=["GET","POST"])
def index():
	colleges = connection.colleges_holder.colleges.find()
	if request.method == 'POST':
		colleges = connection.colleges_holder.colleges.find()
		search_input = request.form['search']
		college_found = search(search_input, colleges)

		return render_template("college.html", search_input=search_input, colleges=colleges, college_found=college_found)

	return render_template("index.html", colleges=colleges)



#@app.route("/signup", methods=["GET","POST"])
#def signup():
#	return render_template("signup.html")

"""@app.route("/signedup", methods=["GET","POST"])
def signedup():
	email = request.form['email']
	username = request.form['username']
	password = request.form['password']
	phone = request.form.get('phone')

	if not session.get("logged_in"):
		insert_account_holder(name,acceptance_rate,location,sat_score,act_score)
	return render_template("homepage.html",username=username) 

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/directory/<username>")
def directory(username):
	contacts = select_by_username_contact(username)
	return render_template("directory.html",username=username,contacts=contacts)"""

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run()