from flask import Flask

"""
1. This line creates an instance of the Flask class
2. It will be our 'web server gateway interface' (wsgi) application.
3. WSGI is a standard protocol that allows the Flask app to interact &
communicate with the underlying web server
4. '__name__' parameter is the built in variable that tells Flask the 
module's name and helping it locate resources like templates
or static files.
"""
app = Flask(__name__)


"""
Routing & Decorators
1. '@app.route()' is a Flask decorator used to bind a specific URL path 
to a python funcn.
2. The 1st param passed into it is the 'rule' which 
written as a string.
3. Working: When a user visits this specific URL path in their 
browser, the decorator intercepts the request and triggers the 
function immediately below it.
4. The string returned by the function is what gets displayed on
the user's web page.
5. Both the route path and the function name MUST be unique. (IMP)
Duplicate function names across different routes will give a routing error.
"""
@app.route("/") # "/" represent the base URL/ Home Page
def welcome():
    return "Welcome to the Home Page, it is under the root path /"

@app.route("/gallery")
def gallery():
    return "Welcome to the Gallery page"

"""
Entry point and Server Execution
1. 'if __name__ == "__main__": serves as the standard entry point for
any Python script.
2. It ensures that the code block inside it only executes if this
specific file ('app.py') is run directly (e.g., via `python app.py`), 
rather than being imported elsewhere.
"""
if __name__ == "__main__":

    """
    app.run()
    1. 'app.run()' starts local development server of Flask
    2. By default it hosts the app on Localhost (127.0.0.1)
    using Port 5000.
    3. We can also pass optional parameters here like 
    'host' (as a string) and 'port' (like port=8080).

    When deploying on cloud envs we will often need to bind 
    it to '0.0.0.0' like 'app.run(host='0.0.0.0', port=5000)'
    so it can listen to external network requests globally.
    
    4. If 'debug=True': It does two main things:
      a. Live Reloading that is the server automatically detects
        any code changes you save and restarts itself instantly
        so that we don't have to manually restart it in the terminal.
      b. Active Debugger means it provides interactive error tracking
        on the web page if something breaks.
    """
    app.run(debug= True)
