from flask import Flask

app = Flask(__name__) # Name of the current file

@app.route("/") # http://127.0.0.1:5000/
def start():
    app.logger.debug("Entry to the init path /")
    return "<p>Hello World</p>"

if __name__ == "__main__":
    app.run(debug=True)