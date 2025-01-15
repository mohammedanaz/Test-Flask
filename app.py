from flask import Flask, request

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    return '<h1>Hello world!!!!</h1>'


@app.route('/querry')
def querry():
    test = request.args.get('test')
    return f'{test}'


if __name__ == '__main__':
    app.run(debug=True)