import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
#db_drop_and_create_all()

## ROUTES
'''
@TODO implement endpoint

    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/api/drinks', methods=['GET'])
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


'''
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/api/drinks/<int:drink_id>', methods=['GET'])
def get_drinks_detail(drink_id):
    drink = Drink.query.filter_by(id=drink_id).first()
    try:
        if drink is None:
            abort(404)
        
        return jsonify({
            "code": 200,
            "success": True,
            "drinks": drink.long()
        })
    except:
        abort(404)

'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''
@app.route('/api/drinks/create', methods=['POST'])
def post_new_drinks():
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
    

'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''
@app.route('/api/drinks/<int:drink_id>', methods=['PATCH'])
def patch_drinks(drink_id):
    code = 200

    try:
        drink = Drink.query.filter_by(id=drink_id).first()

        res = request.get_json()
        edit_title = res.get("title", None)
        edit_recipe = res.get("recipe", None)
        
        if not drink:
            code = 404
            abort(code)
        else:
            drink.title = edit_title
            drink.recipe = edit_recipe
            drink.update()
    
            return jsonify({
                "code": code,
                "success": True,
                "drinks": drink.long()
            })
    except:
        code = 404
        abort(code)

'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''
@app.route('/api/drinks/<int:drink_id>', methods=['DELETE'])
def delete_drink(drink_id):
    code = 200
    try:
        drink = Drink.query.filter_by(id=drink_id).first()

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
        code = 404
        abort(code)

@app.route('/api/auth', methods=['DELETE'])
@requires_auth('post:drinks')
def auth(jwt):
    print(jwt)
    return  "Not implemented, yet"

## Error Handling

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": "Method Not Allowed"
    }), 405

@app.errorhandler(406)
def data_not_acceptable(error):
    return jsonify({
        "success": False,
        "error": 406,
        "message": "Data Not Acceptable"
    }), 406

'''
@TODO implement error handler for AuthError
    error handler should conform to general task above 
'''
