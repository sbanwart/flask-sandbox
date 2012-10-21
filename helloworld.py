from flask import Flask, flash
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Hello World, again!"

if __name__ == "__main__":
    app.run(debug=True)
