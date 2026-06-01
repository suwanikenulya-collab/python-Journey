from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/about", methods=["GET", "POST"])
def about():
    user_input=""
    if request.method == "POST":
        user_input = request.form.get("xss_input", "")
    return render_template("about.html", user_input=user_input)
@app.route("/login", methods=["GET", "POST"])
def login():
    user_input=""
    if request.method == "POST":
        user_input = request.form.get("username", "")
    return render_template("login.html",user_input="")

if __name__ == "__main__":
    app.run(debug=True)