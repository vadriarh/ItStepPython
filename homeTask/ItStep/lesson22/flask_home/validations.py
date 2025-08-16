from flask import request, jsonify
from utils import convert_error_to_json
from models import User

def validation_content_type(in_request: request):
    c_type = in_request.headers.get("Content-Type","")
    if not c_type or not c_type.lower().startswith("application/json"):
        error = "Unsupported Media Type"
        details = "Content-Type must be application/json"
        return jsonify(convert_error_to_json(error, details)), 415
    return None

def validate_user(user:User):
    if not user:
        error = "User not found"
        details = "User with given id does not exist"
        return jsonify(convert_error_to_json(error, details)), 404
    return None

def validate_name_years(name:str,years:int):
    if name is None or years is None:
        error = "Invalid request"
        details = "Required fields: name, years"
        return jsonify(convert_error_to_json(error, details)), 400
    return None

def validate_name(name:str):
    if not isinstance(name,str):
        error = "Invalid name"
        details = "Name must be string"
        return jsonify(convert_error_to_json(error, details)), 400
    if name.strip() =="":
        error = "Invalid name"
        details = "Name must be non-empty string"
        return jsonify(convert_error_to_json(error, details)), 400
    return None

def validate_years(years:int):
    if not isinstance(years,int):
        error = "Invalid years"
        details = "Years must be integer"
        return jsonify(convert_error_to_json(error, details)), 400
    if years < 1:
        error = "Invalid years"
        details = "Years must be >= 1"
        return jsonify(convert_error_to_json(error, details)), 400
    return None