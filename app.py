from flask import Flask, request
import socket
import logging

app = Flask(__name__)
hostname = socket.gethostname()

@app.route("/hello")
def hello_world():
    return f'Hello World! - Host: {hostname}'

@app.route("/health", methods=['GET'])
def health():
    return f'Health - Host: {hostname}'

@app.route("/")
def root():
    logging.info("Incoming request headers: ")
    for header, value in request.headers.items():
        logging.info(f" {header}: {value}")
    return f'Root path - Host: {hostname}'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=8000)