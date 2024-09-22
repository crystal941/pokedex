from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def create_app():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='localhost', port=5000, threaded=False)
