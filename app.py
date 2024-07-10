from flask import (Flask, render_template, request)


#host, port, isDebug = ('192.168.1.159', 8000, True)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    #app.run(host=host, port=port, debug=isDebug)
    app.run()
