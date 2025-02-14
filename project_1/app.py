"""-----What will I learn in this project-----
- 1. What is Flask?
- 2. Setting Up Flask
- 3. Creating My First Flask Route
- 4. Understanding Flask Templates
- 5. Project 1: Hello Flask App
"""
# 1. What is Flask?
# Flask Basics
# - Flask is a lightweight and flexible web framework for developing web applications in Python.  
#   It is a micro web framework designed to be simple, lightweight, and highly customizable.  
# - Flask is often used for building APIs, dynamic websites, and microservices.  

# Why use Flask?  
# - It is lightweight, requiring minimal boilerplate code, which we will explore.  
# - It is scalable and easily expandable for larger projects.  
# - It supports extensions for advanced features.  
# - It is Pythonic, meaning it integrates easily with Python libraries.

# 2. Setting Up Flask 
# - Install Flask: pip3 install flask => python3 -m flask --version (for checking)

# 3. Creating My First Flask Templates  
# A route in Flask maps a URL path to a Python function.  
# It's similar to a folder structure that defines where the elements are located.  
# This is what is called a route.  
# It represents a specific URL path.  

# I will create an app.py file.

from flask import Flask, render_template

# Create Flask App
app = Flask(__name__)

# Define a Route
@app.route("/")
def hello():
    # return "Hello, Nguyen Ho!"
    return render_template("index.html", name="Nguyen Ho")

# Greeting Route
@app.route("/greet/<name>")
def greet(name):
    return render_template("greet.html", name=name)


# Run the App
if __name__ == "__main__":
    app.run(debug=True) # This is for running locally.

# That's the app debug mode is on.
# Do not use it in production deployment.
# Use a production Wsgi server instead.
# And "* Running on http://127.0.0.1:5000" this particular URL, this is the URL that I have.

# 4. Understanding Flask Templates
# In this section, I will create an index.html file. 
# Adding: 
# - The "render_template" function.
# - HTML for the index.html file.
# - Using "render_template".

# 5. Project 1: Hello Flask App
# I will create a new file which is greet.html.