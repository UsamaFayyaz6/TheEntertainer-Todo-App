'''
Todo APP
'''

from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, marshal_with

from common.authentication import auth
from common.helper import parser, todo_item_fields, check_todo_exist

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

class TodoItem(db.Model):
    """
    Todo Item Model
    """
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    created_on = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f'Todo: {self.todo}'

    def as_dict(self):
        """
        Model to dictionary
        """
        return {
            'id': self.id,
            'todo': self.todo,
            'description': self.description,
            'created_on': self.created_on
        }


class TodoListCreate(Resource):
    """
    This resource class used for get list of todos and create new todo
    """
    @auth.login_required
    @marshal_with(todo_item_fields)
    def get(self):
        """
        This method return all Todo
        """
        return TodoItem.query.all()
    
    @auth.login_required
    @marshal_with(todo_item_fields)
    def post(self):
        """
        This method create new todo
        """
        data = parser.parse_args()
        new_todo = TodoItem(todo=data['todo'], description=data['description'])
        db.session.add(new_todo)
        db.session.commit()
        return new_todo
    

class TodoRetriveUpdateDelete(Resource):
    """
    This resource class used for retrive, update and delete todo
    """
    
    @auth.login_required
    @marshal_with(todo_item_fields)
    def get(self, todo_id):
        """
        This method return single todo against todo_id
        """
        result = check_todo_exist(TodoItem, todo_id)
        return result

    @auth.login_required
    @marshal_with(todo_item_fields)
    def put(self, todo_id):
        """
        This method update todo item against todo_id
        """
        todo_item = check_todo_exist(TodoItem, todo_id)
        data = parser.parse_args()
        todo_item.todo = data['todo']
        todo_item.description = data['description']
        db.session.commit()
        return todo_item, 201

    @auth.login_required
    def delete(self, todo_id):
        """
        This method delete todo item against todo_id
        """
        todo_item = check_todo_exist(TodoItem, todo_id)
        db.session.delete(todo_item)
        db.session.commit()
        return {'message':'Todo Item has been deleted'}, 200

api.add_resource(TodoListCreate, '/todos')
api.add_resource(TodoRetriveUpdateDelete, '/todo/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
