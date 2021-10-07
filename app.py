import os
from flask import Flask, request, jsonify, make_response
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)



from models import ToDo
import schema

db.create_all()

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


@app.route("/api/v1/todos/<id>", methods=['DELETE'])
def delete_todo(id):
    if request.method == 'DELETE':
        todo = ToDo.query.get(id)
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
        todos = ToDo.query.all()
        serialized_todos = []
        for todo in todos:
            serialized_todos.append(schema.toDoSchema.dump(todo))
        return make_response(jsonify(serialized_todos))


@app.route("/api/v1/todos/<id>", methods=['PUT'])
def update_todo(id):
    if request.method == 'PUT':
        data = request.get_json()
        todo = ToDo.query.get(id)
        if data.get("content"):
            todo.content = data['content']
        if data.get('title'):
            todo.title = data['title']
        if data.get('author'):
            todo.author = data['author']
        todo.save()
        return make_response(jsonify({"Message": "item has been updated successfully"}))


@app.route("/api/v1/todos/<id>", methods=['GET'])
def get_todo(id):
    if request.method == 'GET':
        try:
            return make_response(schema.toDoSchema.dump(ToDo.query.get(id)))
        except:
            return make_response(jsonify({"Message:Todo does not exist"}))


if '__name__' == '__main__':
    app.run(debug=True)
