from app import db, app

from flask import jsonify,request,url_for

from app.models import User



@app.route('/user/<id>', methods=["GET"])
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])



@app.route('/user', methods=['POST'])
def create_user():
    user = User()
    data = request.get_json() or {}
    user.from_dict(data)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201
    # response.headers['Location'] = url_for('api.get_user', id=user.id)
    return response


@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    user.delete()
    return jsonify([u.to_dict() for u in User.query.all()])


@app.route('/user/<id>/rating', methods=["GET"])
def get_rating(id):
    return jsonify(User.query.get_or_404(id).to_dict())

@app.route('/user/<id>/rating', methods=["DELETE"])
def delete_rating(id):
    pass

@app.route('/user/<id>/rating', methods=["PUT"])
def update_rating(id):
    user =User.query.get_or_404(id)
    data = request.get_json()
    user.from_dict(data)
    db.session.commit()
    return jsonify(user.to_dict())


@app.route('/')
def api_root():
    return "Welcome"