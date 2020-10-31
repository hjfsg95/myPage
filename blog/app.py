from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wine')
def wine():
    return render_template('wine.html')

if __name__ == '__main__':
    app.run(debug=True)