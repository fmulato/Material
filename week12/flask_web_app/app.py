from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/logo')
def logo():
    return render_template('logo.html')

@app.route('/username/<name>')
def learn(name):
    #return f"{name} is learning Flask"
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask Learning</title>
        <style>
            body {{text-align: center;
            }}
            h1 {{
            }}
            p {{font-size: 1em;
            }}
        </style>
    </head>
    <body>
        <h1>Welcome to Flask Learning!</h1>
        <p><strong>{name}</strong> is learning Flask.</p>
        <button onclick="window.location.href='/'">Return to Home Page</button>
    </body>
    </html>
    """

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name','age')
    if name:
        return redirect(url_for('learn', name=name))
    return "Name is required!", 400

@app.route('/<name>/<int:number>')
def learn_waketime(name, number):
     return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask Learning</title>
        <style>
            body {{text-align: center;
            }}
            h1 {{
            }}
            p {{font-size: 1em;
            }}
        </style>
    </head>
    <body>
        <p><strong>{name}</strong> is learning Flask.He/She wakes up at {number} every day!</p>
        <button onclick="window.location.href='/'">Return to Home Page</button>
    </body>
    </html>"""

if __name__ == '__main__':
    app.run(debug=True)
