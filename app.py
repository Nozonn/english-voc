from flask import (Flask, render_template, request)


host, port, isDebug = ('192.168.1.159', 8000, True)

class App:
    app = Flask(__name__)
    def __init__(self) -> None:
        pass
    


    @app.route('/')
    def index():
        return render_template("index.html")


    def run(self, host, port, isDebug):
        self.app.run(host=host, port=port, debug=isDebug)



if __name__ == '__main__':
    app = App()
    app.run(host, port, isDebug)
