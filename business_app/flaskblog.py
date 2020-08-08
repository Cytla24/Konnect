from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'a69c9d16d5fdba9c7151e63b2785fd62'
posts = [
    {
        'author': '@jioke',
        'title': 'Twitter',
        'content': '#HoChi today smacked! #RateKonnect',
        'date_posted': 'December 29, 2019'
    }, 
    {
        'author': '@tammmm',
        'title': 'Twitter',
        'content': 'My #HoChi fries were soggy today :( #RateKonnect',
        'date_posted': 'January 23, 2020'
    },
    {
        'author': '@Ajay',
        'title': 'Twitter',
        'content': '#HoChi meals are so filling! #RateKonnect',
        'date_posted': 'February 1, 2020'
    },
    {
        'author': '@sba',
        'title': 'Twitter',
        'content': 'I\'m addicted to Mumbo Sauce!!! #HoChi #RateKonnect',
        'date_posted': 'February 14, 2020'
    },
    {
        'author': '@collin$',
        'title': 'Twitter',
        'content': 'I can\'t decide what I love more about #HoChi, the food or the pricing? #RateKonnect',
        'date_posted': 'February 29, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
