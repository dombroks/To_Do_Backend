import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import date

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
from models import ToDo

migrate = Migrate()
migrate.init_app(app, db)


@app.route("/")
def index():
    return "Home Page"


@app.route("/create_item", methods=['POST'])
def create_item():
    if request.method == 'POST':
        args = request.args
        todo = ToDo(title=args
                    .get('title'), content=args
                    .get('content'), author=args
                    .get('author'))
        todo.save()
    return jsonify({
        'Message': 'ToDo has been saved successfully'
    })


@app.route("update_item/", methods=['PUT'])
def update_item():
    if request.method == 'PUT':
        args = request.args
        ToDo.query.get(args.get("id"))


if '__name__' == '__main__':
    app.run(debug=True)
