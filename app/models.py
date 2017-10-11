from app import app, bcrypt, db
from flask import jsonify

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)

    def __init__(self, username, password, email, id=None):
        self.username = username
        self.password = bcrypt.generate_password_hash(password)
        self.email = email
        self.id = id

    @staticmethod
    def validate(username, password):
        try:
            authuser = User.query.filter_by(username=username).first()
            pwauth = bcrypt.check_password_hash(authuser.password, password)
            if authuser and pwauth:
                return {'status': True, 'credentials': authuser.id, 'user': authuser}
            else:
                return {'status': False, 'failed': 'Invalid password.'}
        except:
            return {'status': False, 'failed': 'Invalid username.'}

@app.route('/create')
def create_tables():
    try:
        db.create_all()
        return jsonify({'status':'Tables have been created.'})
    except Exception as e:
        return jsonify({'error':str(e)})
