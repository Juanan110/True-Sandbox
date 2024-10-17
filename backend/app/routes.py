from flask import jsonify, request
from . import db
from .models import Cat, Visitor

@bp.route('/cats', methods=['GET'])
def get_cats():
    cats = Cat.query.all()
    return jsonify([cat.name for cat in cats])

@bp.route('/cats', methods=['POST'])
def add_cat():
    data = request.get_json()
    new_cat = Cat(name=data['name'], age=data['age'], breed=data['breed'])
    db.session.add(new_cat)
    db.session.commit()
    return jsonify({'message': 'Cat added'}), 201
