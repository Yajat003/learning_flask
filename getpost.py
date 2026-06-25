from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/") # "/" represent the base URL/ Home Page
def welcome():
    # Returning raw HTML directly inside the return statement
    return "<html><H1>Welcome to the Flask App, it is under the root path '/'</H1></html>"

"""
HTTP Verbs: 'GET' Method
1. HTTP verbs define the core actions a web app can take 
that is GET, POST, PUT & DELETE
2. The 'methods' param inside the decorator explicitly 
restricts what actions this route accepts
3. By default if the 'methods' parameter is omitted like in 
the "/about" route below, Flask defaults to ["GET"].
4. Example: A GET request is like navigating to google.com
We hit a URL, and you receive content 
We aren't pushing new information to the database; 
we're just fetching or 'getting' data.
"""
@app.route("/index", methods = ["GET"])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

"""
Handling Multiple HTTP methods & Form Submission
1. The "/form" route accepts BOTH "GET" and "POST" requests
so this allows a single route to deliver the form AND process
the submitted data.
2. Example: A POST request is like typing a query into 
Google Search and hitting enter, we're packaging user input (data)
and transmitting it to the server to process, search, or store
3. Logic of the function below:
  i. Initial Visit (GET request): When we first navigate to `/form`,
    `request.method == "POST"` is False
    So the code skips the if-block and drops down to execute 
    `render_template("form.html")`.
  ii. Form Submission (POST request): When we fill out the 
    text box and click on "Submit" the browser re-targets this exact 
    route but as a POST request and the if-condition handles it instantly
"""
@app.route("/form", methods = ["GET", "POST"])
def form():
    if request.method == "POST":
        """
        Capturing Form I/P
        1. 'request.form' is a dictionary-like structure containing all
            form fields submitted via POST
        2. The key used inside the bracket notation (["name"]) MUST 
            match the 'name' attribute declared in the HTML input 
            tag (`name="name"`) and NOT the 'id' attribute.
        """
        name = request.form["name"]
        return f"Whatup {name} dawg!  "
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug= True)
