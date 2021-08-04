from flask import Flask, render_template, request
import joblib

# initialize the app
app = Flask(__name__)

# load the model
model = joblib.load('dib_79.pkl')

@app.route('/')
def hello():
    return render_template('form.html')

# @app.route('/home')
# def home():
#     return render_template('index.html')

# @app.route('/contact')
# def contact():
#     return 'Contact Page'

@app.route('/submit', methods = ["POST"])
def form_data():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    # Predict and display the output

    output = model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])

    if output[0] == 1:
        out = 'Diabatic'
    else:
        out = 'Non Diabatic'

    return render_template('index.html', data = f'The person is {out}')

    return 'Form Submitted'

if __name__ == '__main__':
    app.run(debug = True)