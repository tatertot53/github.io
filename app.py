# import necessary libraries
from flask import Flask, render_template, jsonify, redirect
# import pymongo
from flask_pymongo import PyMongo
import scrape_mars


# create instance of Flask app
app = Flask(__name__)

mongo = PyMongo(app)

# create route that renders index.html template
@app.route("/")
def index():
	mars_data = mongo.db.mars_db.find_one()
	return render_template("index.html", mars_data=mars_data)

@app.route("/scrape")
def scrape():
	mars = mongo.db.mars_db
	data = scrape_mars.scrape()
	mars.update(
		{},
		data,
		upsert=True
	)
	return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
	app.run(debug=True)