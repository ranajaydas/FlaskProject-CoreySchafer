from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm           # user created module and classes
app = Flask(__name__)

app.config['SECRET_KEY'] = '0bbe7a69ad9ecf8eced7a362d7948e4c'

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


if __name__ == '__main__':
    app.run(debug=True)
