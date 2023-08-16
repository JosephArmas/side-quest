from flask import Blueprint, request
from sqlalchemy.exc import SQLAlchemyError

from Managers.RegisterManager.RegisterManager import RegisterManager
from Services.RegisterService.RegisterService import RegisterService

register_bp = Blueprint('registration', __name__)
r_service = RegisterService("DEV_SQL_USER")
r_manager = RegisterManager(r_service)


@register_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password: str = data.get('password')
    try:
        result = r_manager.create_user(email, password)
        return result.message
    except SQLAlchemyError as e:
        print("Error in Creating user")
