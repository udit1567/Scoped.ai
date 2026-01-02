from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app,origins='*')



    return app

app = create_app()


@app.route('/')
def pro():
    return 'hello'



if (__name__ == '__main__'):
    app.run(debug=True)
