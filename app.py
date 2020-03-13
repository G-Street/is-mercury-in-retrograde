from flask import Flask, jsonify
from flask_cors import CORS
import astro

#configuration
DEBUG = True

#instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

#enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Sanity check route
@app.route("/home", methods=['GET'])
def pullFromSource():
    return jsonify(astro.get_MercRet())

if __name__ == "__main__":
  app.run()
