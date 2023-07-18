import os
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient

app = Flask(__name__)
load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))
centers = client["data"]["centers"]


@app.route("/centers")
def index():
    response = centers.find({}, {"_id": 0}).sort("id", 1)
    return list(response)


@app.route("/centers/<int:id>")
def show(id):
    response = centers.find_one({"id": id}, {"_id": 0})
    return response


if __name__ == "__main__":
    app.run(debug=True)
