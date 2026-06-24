from flask import Flask

"""
This line creates an instance of the Flask class
It will be our 'web server gateway interface' (wsgi) application.
"""
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the Home Page, it is under the root path /"

@app.route("/gallery")
def gallery():
    return "Welcome to the Gallery page"

if __name__ == "__main__":
    app.run(debug= True)
