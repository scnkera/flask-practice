from flask import Blueprint, abort, make_response, request
from ..db import db
from app.models.cat import Cat
# from ..models.cat import cats

cats_bp = Blueprint("cats_bp", __name__, url_prefix="/cats")

@cats_bp.get("")
def create_cat():
    request_body = request.get_json()
    name: request_body["name"]
    color: request_body["color"]
    personality: request_body["personality"]

    new_cat = Cat(name=name, color=color, personality=personality)
    db.session.add(new_cat)
    db.session.commit()

    response = new_cat.to_dict()
    return response, 201

# @cats_bp.get("")
# def get_all_cats():
#     results_list = []

#     for cat in cats:
#         results_list.append(cat.to_dict())
    
#     return results_list

# @cats_bp.get("/<cat_id>")
# def get_one_cat(cat_id):
#     cat = validate_cat(cat_id)
#     return cat.to_dict(), 200


# def validate_cat(cat_id):
#     try:
#         cat_id = int(cat_id)
#     except:
#         abort(make_response({"message":f"Cat id {cat_id} invalid"}, 400))
    
#     for cat in cats:
#         if cat.id == cat_id:
#             return cat
    
#     abort(make_response({ "message": f"Cat {cat_id} not found"}, 404))


