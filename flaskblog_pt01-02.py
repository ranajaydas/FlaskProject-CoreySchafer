from flask import Flask, render_template, url_for

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
