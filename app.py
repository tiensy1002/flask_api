from flask import Flask
from api import api_v2, learn_blueprint

# def create_app():
#     app = Flask(__name__)
#     app.register_blueprint(learn_blueprint)
#     api = api_v2

#     api.init_app(app)

#     return app

app = Flask(__name__)
app.register_blueprint(learn_blueprint)
app.run(debug=True)