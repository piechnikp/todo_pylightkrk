from project import db

class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String(250), index=False, unique=False)
    done = db.Column(db.Boolean, index=False, unique=False, default=False)

    def __repr__(self):
        return '<todo {}>'.format(self.msg)