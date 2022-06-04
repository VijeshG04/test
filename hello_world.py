from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return('Happy sunday. Have a good day')

@app.route('/login')
def login():
    return('Please enter your login')

@app.route('/contact')
def contact():
    return('This is my contact details')

app.run(debug=True)