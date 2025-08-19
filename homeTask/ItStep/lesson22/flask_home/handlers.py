from flask import jsonify
from flask_jwt_extended import JWTManager

jwt = JWTManager()

def init_jwt_handlers(app):
    jwt.init_app(app)

    @jwt.unauthorized_loader
    def handle_unauthorized(err_msg):
        return jsonify ({"err":"Missing or invalid authorization header","detail":err_msg}), 401

    @jwt.expired_token_loader
    def handle_expired_token(jwt_header,jwt_payload):
        return jsonify({"err": "Expired token"}), 401