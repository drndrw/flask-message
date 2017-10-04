from flask import jsonify
from app import app

@app.route('/')
def apptest():
    return jsonify({'test':'hey'})
