from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')

def root():
    return make_response("Hello World in Python", 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
