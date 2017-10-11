from flask import jsonify, request
from flask_restful import Resource, Api
from app import api, app, db, models


@app.route('/')
def apptest():
    return jsonify({'test':'hey'})

class Users(Resource):

    def get(self):
        users = models.User.query.all()
        if users:
            return jsonify([{'username':user.username,'id':user.id} \
                for user in users])
        else:
            return {'error':'There are no users.'}

    def post(self):
        data = request.get_json()
        print (data)
        if data['username'] and data['password'] and data['email']:
            try:
                newuser = models.User(data['username'],data['password'],data['email'])
                db.session.add(newuser)
                db.session.commit()
                return {'status':'Successfully created {}.'.format(data['username'])}
            except Exception as e:
                return {'error':'An error has occured.','info':str(e)}
        else:
            return {'error':'Please enter all required fields.'}

    def put(self):
        data = request.get_json()
        response = models.User.validate(data['username'], data['password'])
        if response['status']:
            return {'status':'Logged in.', 'userid': response['credentials']}
        else:
            return {'error':'Invalid credentials.', 'reason': response['failed']}

class UserQuery(Resource):

    def get(self, userid):
        authuser = models.User.query.filter_by(id=userid).first()
        if authuser:
            return {'username': authuser.username, 'id': authuser.id}
        else:
            return {'error': 'Invalid user id.'}

api.add_resource(Users,'/user')
api.add_resource(UserQuery,'/user/<userid>')
