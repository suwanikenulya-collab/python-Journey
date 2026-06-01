from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"


@app.route("/secure")
def secure():
    return "welcome to Secure Password Generator"


@app.route("/about", methods=["GET", "POST"])
def about():

    user_input = ''

    if request.method == "POST":
        user_input = request.form.get('xss_input', '')


    return render_template("about.html", user_input=user_input)


if __name__ == "__main__":

    app.run(debug=True)