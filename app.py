from flask import Flask

app = Flask(__name__) # app is object of the class "Flask"

@app.route("/") # empty route / homepage
def hello(): # when this url is accessed...
    return "Hello world!"

if __name__ == "__main__": # this runs w app.py while the routes dont
    app.run(host="0.0.0.0", debug=True) 
    # since the conditional above would always be true in our case, then this always executes w app.py
    # debug mode being True makes it so that you dont need to execute py again to see changes, just refresh