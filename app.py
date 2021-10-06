import os

from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

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


@app.route("/api/v1/todos", methods=['POST'])
def create_todo():
    if request.method == 'POST':
        args = request.args
        todo = ToDo(title=args.get('title'),
                    content=args.get('content'),
                    author=args.get('author'))
        try:
            todo.save()
        except:
            return jsonify({
                'Message': 'An error, something went wrong during saving'
            })

        return jsonify({
            'Message': 'ToDo has been saved successfully'
        })


@app.route("/api/v1/todos", methods=['DELETE'])
def delete_todo():
    if request.method == 'DELETE':
        args = request.args
        todo = ToDo.query.get(args.get('id'))
        try:
            todo.delete()
        except:
            return jsonify({
                'Message': 'ToDo does not exist'
            })

        return jsonify({
            'Message': 'ToDo has been deleted successfully'
        })


@app.route("/api/v1/todos", methods=['GET'])
def get_todos():
    if request.method == 'GET':
        todos = ToDo.get_all()
        return make_response(jsonify({"todos": todos}))


if '__name__' == '__main__':
    app.run(debug=True)
