from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run()
    