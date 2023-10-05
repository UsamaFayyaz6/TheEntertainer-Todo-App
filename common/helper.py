'''
Todo Helper 
'''

from flask_restful import reqparse, fields, abort
from common.encryption import encrypt_response_func

# Used for parse request and validate payload data
parser = reqparse.RequestParser()
parser.add_argument('todo', type=str, required=True, help='Todo is required')
parser.add_argument('description', type=str, help='Description is required')

# Used for marshall fields
todo_item_fields = {
    # 'id': fields.Integer,                # This lines commented because we encrypt response into string
    # 'todo': fields.String,               # and return into encrypted_response
    # 'description': fields.String,
    # 'created_on': fields.DateTime,
    'encrypted_response': fields.String,
}

def check_todo_exist(todo_model, todo_id):
    """
    This function is used for check todo is exist or not in Database
    """

    todo_item = todo_model.query.get(todo_id)
    if todo_item is None:
        abort(404, encrypted_response = encrypt_response_func("Todo id {} doesn't exist".format(todo_id)))

    return todo_item

