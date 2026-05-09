from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
    return 'hello world'
@app.route("/secure")
def secure():
    return f'welcome to Secure Password Generator'

if __name__ == "__main__":
    app.run(debug=True)


#implement a template folder and put the index.html file there.(where the web application works.)
#@app.route("/")
#def home():
 #   return render_template('index.html')

#implement another folder to add-on other style files, images ...

#@app.route("/secure")
#def secure():
 #   render_template("secure.html")
    #html files should be in template folder(same folder)