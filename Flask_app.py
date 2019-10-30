from flask import Flask, render_template, url_for, redirect, flash
from forms import RegistrationForm, LoginForm

posts = [
    {
        'author':'Matt Crichton',
        'title':'Web Dev Journey',
        'content':'I love learning Flask!',
        'date_posted':'October 20, 2019',
    },
    {
        'author':'John Doe',
        'title':'Also a Web Dev',
        'content':'Prefers ReactJS over Flask',
        'date_posted':'October 21st, 2019',
    }
]

# Creating the flask app and storing in the app variable
app = Flask(__name__)

app.config['SECRET_KEY'] = 'e8eacad2cc5115ed994c22f08daa5a22'

# Adding a route decorator for the site, both the routes are handled by the same decorator.
# Both lead users to the home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)
    # The above posts var is from the posts list above, and is being passed
    #  to the 'home.html' template.

# Creating a route to the about page
@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

# Conditional is only true if we run the script directly with Python
# It gives us some extra functionality later when debugging
if __name__ == '__main__':
    app.run(debug=True)