from flask import Flask, request, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    value = [1, 2, 3, 4, 5]
    return render_template('index.html', value=value)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        print('request.form - ', request.form)
        username = request.form.get('username')
        password = request.form.get('password')

        return redirect(url_for('dashboard', username=username) )
    return render_template('login.html')

@app.route('/dashboard', methods=['GET',])
def dashboard():
    username = request.args.get('username')
    return render_template('dashboard.html', username=username)


if __name__ == '__main__':
    app.run(debug=True)