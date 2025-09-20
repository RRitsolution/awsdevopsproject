from flask import Flask

app = Flask(__name__)


@app.route("/")

def nirmal():
 
    return "<p> Hi Welcome to Backend</p>"


@app.route("/nirmal/")

def backend():

    return '<p><a href="https://www.youtube.com/@Nirmaltechnical06" target="_blank">Visit My Channel</a></p>'

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5000)

