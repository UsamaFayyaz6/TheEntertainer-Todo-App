'''
Todo Model APP
'''

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from datetime import datetime

class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    created_on=db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f'Todo: {self.todo}'
    
    def as_dict(self):
        return {
            'id': self.id,
            'todo': self.todo,
            'description': self.description,
            'created_on': self.created_on
        }