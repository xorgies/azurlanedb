from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/personajes')
def personajes():
    return render_template('personajes.html')

if __name__ == '__main__':
    # PRO
    # app.run()

    # Testing
    app.run(debug=True)
