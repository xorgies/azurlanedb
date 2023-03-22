from flask import Flask, render_template
import os
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/personajes')
def personajes():
    filename = os.path.join(app.static_folder, 'datos/datos.json')
    with open(filename) as blog_file:
        data = json.load(blog_file)

    return render_template('personajes.html', jsonData=data)

if __name__ == '__main__':
    # PRO
    # app.run()

    # Testing
    app.run(debug=True)
