from flask import Flask, request, jsonify, render_template, redirect
import models


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title='Home')


@app.route('/galeria', methods=['GET'])
def galery():
    return render_template('galery.html', title='Galery')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        context = {
            'name': 'Krzysiek & Pablo',
            'surname': 'Wandzlo & Kuczmiklo',
            'passion': 'Rowero & Chesso',
            'email': 'None & None',
            'profession': 'Programmingo & Chessing'
        }

        return render_template('kontakt.html', title='Kontakt', context=context)


@app.route('/calculator', methods=['GET'])
def calculator():
    return render_template('calculator.html', title='Calculator')


@app.route('/programming', methods=['GET'])
def programming():
    context = []
    languages = models.connection('juch')

    for row in languages.execute('SELECT name, description FROM languages'):
        context.append(row)

    return render_template('programming.html', title='Programming', context=context)


if __name__ == '__main__':
    app.run(debug=True)

