from flask import render_template, Blueprint, redirect, url_for
from project.models import Todo
from .forms import AddForm
from project import db


# CONFIG
home_blueprint = Blueprint('home', __name__, template_folder='templates')


@home_blueprint.route('/')
@home_blueprint.route('/index')
def index():
    user = {'username': 'Piotrek'}

    # todos = [
    #     {
    #         'id': 0,
    #         'msg': 'przygotuj sie na pylight',
    #         'done': False
    #     },
    #     {
    #         'id': 1,
    #         'msg': 'Opierdzielaj sie ogladajac anime liczac na to ze uda Ci sie przygotowac prezentacja w locie',
    #         'done': True
    #     }
    # ]

    todos = Todo.query.all()

    return render_template('index.html', title='TODO', user=user, todos=todos)

@home_blueprint.route('/add_todo', methods=['GET', 'POST'])
@home_blueprint.route('/edit_todo/<id>', methods=['GET', 'POST'])
def add_todo(id=None):
    todo = Todo.query.get(id) if id is not None else Todo()
    form = AddForm(obj=todo)

    if form.validate_on_submit():
        form.populate_obj(todo)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('home.index'))

    return render_template('add.html', title='Add new todo', form=form)