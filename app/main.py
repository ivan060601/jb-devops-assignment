import os
from flask import Flask

host = os.getenv("HOST", "0.0.0.0")
port = int(os.getenv("PORT", "8080"))

app = Flask(__name__)

@app.route("/healthCheck")
def health_check():
    return "Ok"

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return "<html><body><h1>Hello world!</h1></body></html>"

if __name__ == "__main__":
    app.run(host=host, port=port)
