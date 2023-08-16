from flask import Flask

from EntryPoint.Controllers.RegisterController import register_bp

app = Flask(__name__)


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'


app.register_blueprint(register_bp)

if __name__ == '__main__':
    app.run()
