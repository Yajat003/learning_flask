from flask import Flask, render_template, request, redirect, url_for
# Imported 'redirect' and 'url_for'.
# 'url_for' is responsible for dynamically building a URL based on a target function name
# 'redirect' takes that dynamically built URL and sends the user's browser there

app = Flask(__name__)

@app.route("/") # "/" represent the base URL/ Home Page
def welcome():
    # Returning raw HTML directly inside the return statement
    return "<html><H1>Welcome to the Flask App, it is under the root path '/'</H1></html>"

@app.route("/index", methods = ["GET"])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')



"""
Variable Rules & Data type restrictions
1. Paths defined as '/route/<score>' treat the parameter as a string by default
2. Prepending a datatype like '/route/<int:score>' creates a 'Variable Rule'
3. This restricts the parameter to that specific data type (e.g., integers only)
4. WARNING: If we specify an integer rule but attempt to directly concatenate it with a string 
  in the Python logic (e.g., "You scored " + score), Flask will throw a TypeError: 
  'Can only concatenate string not integer'
"""
# Variable rule
@app.route('/success/<int:score>')
def success(score):
    # return "You scored " + str(score) + " marks"
    res = "" 
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    # 'results' maps a data variable from backend Python into the HTML template
    return render_template("result.html", results = res)
    
# Variable rule
@app.route('/successresults/<int:score>')
def successresults(score):
    res = "" 
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    
    # Passing complex data structures: A dictionary matching keys to values
    exp = {"score":score, "res":res}
    return render_template("result1.html", results = exp)

# Variable rule
@app.route('/successif/<int:score>')
def successif(score):

    return render_template("result.html", results = score)

# Variable rule
@app.route('/fail/<int:score>')
def fail(score):
    
    return render_template("result.html", results = score)

"""
Action param & Dynamic URL Building
1. When a form submission is received via POST, all inputs are captured as string data by default
2. To run math operations (like calculating an average), you must typecast them using float() or int()
3. Building URL Dynamically: 'url_for' takes the string name of a destination target function 
  (e.g., 'successresults') along with any parameters it requires (e.g., score=total_score)
4. This dynamically constructs the correct URL address and passes it to 'redirect' to route the user
"""
@app.route('/submit', methods = ["POST","GET"])
def submit():
    total_score = 0
    if request.method == "POST":
        # Form values are safely captured via 'request.form' and casted to float data types
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        
        # Computing average marks across four subjects
        total_score = (science + maths + c + data_science) / 4
    else:
        # If the route receives a GET request, simply supply the input form page
        return render_template('getresult.html')
    # Triggers dynamic mapping to send score to successresults
    return redirect(url_for('successresults',score=total_score))

if __name__ == "__main__":
    app.run(debug= True)
