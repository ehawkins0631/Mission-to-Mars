## 10.5.1 - Fask and Mongo
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import Scraping

## 10.5.1 Cont.. 
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
## Python that our app will connect to Mongo using a URI, 
## URI = uniform resource identifier similar to a URL.
## "mongodb://localhost:27017/mars_app" is the URI we'll be using to connect our app to Mongo. 
## This URI is saying that the app can reach Mongo through our localhost server, 
## using port 27017, using a database named "mars_app"
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

## 10.5.1 Cont...
# First, let's define the route for the HTML page. In our script, type the following

@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

# 10.5.1 Cont...
## Our next function will set up our scraping route
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = Scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)

## The final bit of code we need for Flask is to tell it to run
if __name__ == "__main__":
   app.run(debug=True) # 
## Start by using the command line to navigate to your project folder.
##'C:\\Users\\ehawk\\Desktop\\Class Folder\\Class challenges\\Mission-to-Mars\\Scraping.py', reloading
## * Detected change in 'C:\\Users\\ehawk\\Desktop\\Class Folder\\Class challenges\\Mission-to-Mars\\Scraping.py', reloading
## * Detected change in 'C:\\Users\\ehawk\\Desktop\\Class Folder\\Class challenges\\Mission-to-Mars\\Scraping.py', reloading
##* Restarting with watchdog (windowsapi)
## * Debugger is active!
## * Debugger PIN: 133-410-020
## * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)