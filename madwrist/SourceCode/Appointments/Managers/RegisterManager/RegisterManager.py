import random

from CrossCutting.ErrorHandling import ErrorHandling
from CrossCutting.Response import Response
from CrossCutting.Security.GenerateHash import GenerateHash as Gh
from Services.RegisterService.RegisterService import RegisterService


class RegisterManager:
    def __init__(self, register_service: RegisterService):
        self._eh = ErrorHandling()
        self._rservice = register_service

    def create_user(self, email, password):
        valid_email_response = self._eh.is_valid_email(email)
        valid_pw_response = self._eh.is_valid_password(password)
        if not valid_pw_response.is_successful:
            return valid_pw_response.message
        if not valid_email_response.is_successful:
            return valid_email_response.message
        salt = Gh.create_salt()
        hash_pw = Gh.create_hash(password, salt)
        username_splice = email.split('@')
        nums = [(random.randint(0,9)) for i in range(2)]
        username = username_splice[0] + str(nums[0]) + str(nums[1])
        result = self._rservice.register_new_user(username, hash_pw)
        return result





