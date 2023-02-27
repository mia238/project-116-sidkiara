# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Manshi"
    age = "20"

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():

    name = "Bob"
    age = "55"

    return render_template('index.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/mother")
def mother():

    name = "Becky"
    age = "67"

    return render_template('index.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/friend")
def friend():

    name = "Sidharth M"
    age = "38"

    return render_template('index.html' , name = name , age = age)

# add other routes, if you want
@app.route("/friends")
def friends():

    name = "Kiara M"
    age = "30"

    return render_template('index.html' , name = name , age = age)



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
