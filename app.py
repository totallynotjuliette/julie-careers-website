from flask import Flask, render_template

app = Flask(__name__) # app is object of the class "Flask"

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Miami, Florida",
        "salary": "$85,000"
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "Tampa, Florida", 
    },
    {
        "id": 3,
        "title": "Frontend Engineer",
        "location": "Los Angeles, California",
        "salary": "$63,000"
    },
    {
        "id": 4,
        "title": "Backend Engineer",
        "location": "Boston, Massachusetts",
        "salary": "$70,000"
    },
]


@app.route("/") # empty route / homepage
def hello(): # when this url is accessed...
    return render_template("home.html", jobs=JOBS)

if __name__ == "__main__": # this runs w app.py while the routes dont
    app.run(host="0.0.0.0", debug=True) 
    # since the conditional above would always be true in our case, then this always executes w app.py
    # debug mode being True makes it so that you dont need to execute py again to see changes, just refresh
    # remember to open devtools network and disable caching for this alawys to work when updating html