from flask import Flask  #makes the web application -framework

app = Flask(__name__)  #creates the app


@app.route("/")  #defines the homepage
def home():
    return "Hello, world!"


if __name__ == "__main__":
    app.run(debug=True)
