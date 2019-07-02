from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return "this is what ege g you should have done"

@app.route('/store/')
def store():
    return "have done"

@app.route('/ez/')
def ez():
    return "done"

if __name__ == "__main__":
    app.run(port=8080,debug=True) 