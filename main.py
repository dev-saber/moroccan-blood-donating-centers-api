import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from pymongo import MongoClient

app = Flask(__name__)
load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))
centers = client["data"]["centers"]


@app.route("/")
def home():
    data = centers.find()
    # return list(data)
    # Convert ObjectId to string for serialization
    serialized_data = []
    for document in data:
        document["_id"] = str(document["_id"])
        serialized_data.append(document)
    return jsonify(serialized_data)


if __name__ == "__main__":
    app.run(debug=True)
