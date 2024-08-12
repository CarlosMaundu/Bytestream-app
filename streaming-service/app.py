from flask import Flask

app = Flask(__name__)

@app.route('/streaming')
def streaming():
    return "Welcome to the Streaming Service!"

@app.route('/healthz')
def healthz():
    return "OK", 200

@app.route('/ready')
def ready():
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
    