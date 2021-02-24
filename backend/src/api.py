import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)
setup_db(app)
CORS(app)


# if uncomment the following line to initialize the datbase
#db_drop_and_create_all()


## ROUTES

# GET /drinks --> public
# returns status code 200 and json {"success": True, "drinks": drinks} 
# where drinks is the list of drinks or error

@app.route('/drinks', methods=['GET'])
def get_drinks():
    drinks = Drink.query.all()
    if drinks is None:
        abort(404)
 
    drinks_short = []
    for item in drinks:
        drinks_short.append(item.short())

    try:
        return jsonify({
            "code": 200,
            "success": True,
            "drinks": drinks_short,   
        })
    except:
        abort(404)  



# GET /drinks-detail --> private
# returns status code 200 and json {"success": True, "drinks": drinks} 
# where drinks is the list of drinks or error

@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drinks_detail(f):
    try:
        if f is None:
            abort(401)
        
        return jsonify({
            "code": 200,
            "success": True,
            "drinks": [drink.long() for drink in Drink.query.all()]
        })
    except:
        abort(404)


# POST /drinks --> private
# returns status code 200 and json {"success": True, "drinks": drink} 
# where drink an array containing only the newly created drink
# or error code

@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def post_new_drinks(f):
    code = 200
    drink = None
    res = request.json
    new_title = res.get('title', None)
    new_recipe = res.get('recipe', None)
    try:
        if not new_title:
            code = 404
        else:
            drink_exist = Drink.query.filter_by(title=new_title).first()
            if drink_exist is None:
                new_recipe = parse_recipe(new_recipe)
                drink = Drink(title=new_title, recipe=new_recipe)
                drink.insert()
                drink = Drink.query.filter_by(title=new_title).first()
                return jsonify({
                    "code": code,
                    "success": True,
                    "drinks": drink.long()
                })  
            else:
                code = 406
    except:
        code = 422
    abort(code)
    

# PATCH /drinks/<id> --> private
# Input: where <id> is the existing model id
# returns status code 200 and json {"success": True, "drinks": drink}
# where drink an array containing only the updated drink or error code
    
@app.route('/drinks/<int:drink_id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def patch_drinks(f, drink_id):
    code = 200
    res = request.json
    new_title = res.get('title', None)
    new_recipe = res.get('recipe', None)
    try:
        drink = Drink.query.filter(Drink.id == drink_id).one_or_none()
        if drink:
            drink_title_exist = Drink.query.filter_by(title=new_title).first()
            if drink_title_exist:
                code = 406
                abort(code)
            if new_recipe:
                new_recipe = parse_recipe(new_recipe)
                drink.recipe = new_recipe
            if new_title:
                drink.title = new_title
            drink.update()
            return jsonify({
                "code": code,
                "success": True,
                "drinks": drink.long()
            })
        else:
            code = 404
            abort(code)
    
    except:
        code = 422
        abort(code)


# DELETE /drinks/<id> --> private
# returns status code 200 and json {"success": True, "delete": id} 
# where id is the id of the deleted record or error code

@app.route('/drinks/<int:drink_id>', methods=['DELETE'])
# @requires_auth('delete:drinks')
def delete_drink(drink_id):
    code = 200
    drink = Drink.query.filter(Drink.id==drink_id).one_or_none()
    try:
        print(drink)
        if drink is None:
            code = 404
            abort(code)
        else:
            drink.delete()
            return jsonify({
                "code": code,
                "success": True,
                "delete": drink.id
            })
    except:
        code = 422
        abort(code)


def parse_recipe(recipe):
    if type(recipe) is dict:
        recipe = json.dumps([recipe])
    elif type(recipe) is list:
        recipe = json.dumps(recipe)
    else:
        code = 406
        abort(code)
    return recipe

## Error Handling

@app.errorhandler(401)
def unauthorized_user(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "Unauthorized"
    }), 401

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@app.errorhandler(406)
def data_not_acceptable(error):
    return jsonify({
        "success": False,
        "error": 406,
        "message": "Data Not Acceptable"
    }), 406
    
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


#Error AuthError:

@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response