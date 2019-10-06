from flask import render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm           # user created module and classes
from flaskblog.models import User, Post                           # user created module and classes
from flaskblog import app                                         # user created module and classes


posts = [
    {
        'author': 'Ranajay Das',
        'title': 'My First Post!',
        'content': 'Hello everyone! This is Jojo! BlahBlahBlah...',
        'date_posted': 'Oct 04, 2019'
    },
    {
        'author': 'Choot Pakoda',
        'title': 'Buy My Book!',
        'content': 'Arrey...mera book khareedo yaar!',
        'date_posted': 'Oct 24, 2029'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',
                           posts=posts)


@app.route('/about')
def about():
    return render_template('about.html',
                           title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {}!'.format(form.username.data), 'success')
        return redirect(url_for('home'))
    return render_template('register.html',
                           title='Register',
                           form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Welcome, {}!'.format(form.email.data), 'success')
        return redirect(url_for('home'))
    return render_template('login.html',
                           title='Login',
                           form=form)