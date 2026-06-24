from flask import Flask, render_template

app = Flask(__name__)

"""
Inline HTML Rendering
1. One can directly return raw HTML strings from a func.n, 
and the browser will still parse it.
2. While this works perfectly for rapid testing but it is 
considered a BAD PRACTICE for real world apps because UI 
layouts require hundreds of lines of code.
3. Keeping HTML embedded inside python code ruins readability 
and clean separation of concerns.
"""
@app.route("/") # "/" represent the base URL/ Home Page
def welcome():
    # Returning raw HTML directly inside the return statement
    return "<html><H1>Welcome to the Flask App, it is under the root path '/'</H1></html>"

"""
THE 'templates' Directory Constratin & JINJA2
1. 'render_template('filename.html')' triggers the Flask's underlying 
Jinja2 template engine.
2. CRITICAL FLASK RULE: Flask strictly expects all HTML files to be
stored inside a folder named EXACTLY "templates" in the root directory
of the project.
3. If we misname the folder like "template" or if the file doesn't
exist, Flask will throw a "TemplateNotFound" error.
  
Deafult HTTP Verbs
1. By default every route we create using '@app.route()' handles 
"GET" requests automatically. Advanced HTTP methods like POST, PUT,
or DELETE must be explicitly declared.
"""
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug= True)
