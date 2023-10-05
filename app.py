'''
Todo APP
'''

from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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
        Model to dictionatry
        """
        return {
            'id': self.id,
            'todo': self.todo,
            'description': self.description,
            'created_on': self.created_on
        }


if __name__ == '__main__':
    app.run(debug=True)
