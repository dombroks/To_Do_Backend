from flask_marshmallow.sqla import SQLAlchemyAutoSchema
import models


class ToDoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.ToDo
        fields = ("id", "title", "content", "author", "published")


toDoSchema = ToDoSchema()
