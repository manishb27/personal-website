from flask import Flask

app = Flask(__name__)


@app.route("/")
def Hello():
  return " Hello there How is it going? I am fine"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
