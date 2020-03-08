from flask import Flask
import astro
app = Flask(__name__)


@app.route("/")
def pullFromSource():
    return astro.get_MercRet()
    

if __name__ == "__main__":
  app.run()
