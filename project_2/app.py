"""-----What will I learn in this project-----
- 1. Advanced Flask Routing
- 2. Dynamic Templates with Jinja2
- 3. Passing Data Between Routes and Templates
- 4. Organizing Flask Projects for Scalability 
- 5. Project 2: Personal Blog Website
"""
# 1. Advanced Flask Routing
# from flask import Flask, render_template

# app = Flask(__name__)

# # Static route
# @app.route("/home")                                     # This is a static route.
# def home():
#     return "Welcom to My Blog!"
    
# # Dynamic route
# @app.route("/home/post/<int:post_id>")                  # This is a dynamic route.
# def show_post(post_id):
#     return f"Displaying Post #{post_id}"

# if __name__ == "__main__":
#     app.run(debug=True)

#------------------------------------------------------------------------------------------------------------------------
# 2. Dynamic Templates with Jinja2
# using Jinja2 templates you have variables where you pass data into templates.
# With angular, the curly brackets, curly brackets and the variable name inside with curly closing curly brackets.
# You can also do loops where you render lists from using curly bracket percentage, and inside that you can write a for loop.
# You can display content conditionally by using again that curly bracket percentage.
# And if is what you can use inside there.

# from flask import Flask, render_template

# app = Flask(__name__)

# # Static route
# @app.route("/")
# def home():
#     return render_template("index.html", title="Welcom to my website!")

# if __name__ == "__main__":
#     app.run(debug=True)

#------------------------------------------------------------------------------------------------------------------------
# 3. Passing Data Between Routes and Templates
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     posts = [
#         {"id": 1, "title": "First Post", "content": "This is my first blog post."},
#         {"id": 2, "title": "Exploring Flask", "content": "Today, I learned about Flask web framework."},
#         {"id": 3, "title": "My Coding Journey", "content": "Sharing my experience learning Python."},
#         {"id": 4, "title": "Web Development Tips", "content": "Some useful tips for building websites."},
#         {"id": 5, "title": "Understanding APIs", "content": "A beginner's guide to working with APIs."}
#     ]   
#     return render_template("index.html", posts=posts)

# if __name__ == "__main__":
#     app.run(debug=True)

# ------------------------------------------------------------------------------------------------------------------------
# 4. Organizing Flask Projects for Scalability 
# - I will create a blog_app folder.
# - Inside this folder, I will create an app.py file, as well as templates and static folders.
# - Inside the templates folder, I will create index.html and post.html files.
# - Inside the static folder, I will create a css folder, and inside it, I will create a styles.css file.
# - Summary:
#   * Create a new project named blog_app.
#   * Create app.py: this is the main file.
#   * Templates: contains HTML files.
#   * Static: contains CSS, JavaScript, and images.

# ------------------------------------------------------------------------------------------------------------------------
# 5. Project 2: Personal Blog Website
# - The goal is to build a personal blog website with a homepage displaying a list of blog posts, similar to what we did earlier.
# - Project architecture: 
#   * Create a personal_blog folder, and inside it, add static, templates, and app.py.
#   * Inside the static folder: add styles.css.
#   * Inside the templates folder: add index.html, post.html, and layout.html.
#   * Start coding to complete the project.
