from flask import Blueprint, request
from flask.views import MethodView
from flask import jsonify

from project.models import Todo
from project import db

api_blueprint = Blueprint('api', __name__)


class TodoAPI(MethodView):

    def get(self):
        cols = ['id', 'msg', 'done']
        data = Todo.query.all()
        result = [{col: getattr(d, col) for col in cols} for d in data]
        return jsonify(result)

    def post(self):
        msg = request.values.get('msg', None)
        if msg:
            todo = Todo()
            todo.msg = msg
            todo.done = bool(request.values.get('done', False))
            db.session.add(todo)
            db.session.commit()
            return 'OK'
        else:
            return 'No msg in request params :-('


api_blueprint.add_url_rule('/api/', view_func=TodoAPI.as_view('api'))