from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_flask():
    return "<p>Hello, Flask!</p>"

if __name__ == '__main__':
    hello_flask()

