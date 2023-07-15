import os
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient

app = Flask(__name__)
load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))
centers = client["data"]["centers"]


@app.route("/")
def home():
    response = centers.find({}, {"_id": 0})
    return list(response)


if __name__ == "__main__":
    app.run(debug=True)
