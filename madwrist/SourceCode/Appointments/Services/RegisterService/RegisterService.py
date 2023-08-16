from CrossCutting.Response import Response
from DataAccess.RegisterSqlDao import RegisterSqlDao


class RegisterService:
    def __init__(self, url):
        self._rdao = RegisterSqlDao(url)

    def register_new_user(self, username, hashpw):
        response = Response()
        valid_insert = self._rdao.insert_user(username,hashpw).is_successful
        if valid_insert:
            response.is_successful = True
            response.message = "Successful insert"
            return response
        response.message = "Invalid Insert, please try again"
        return response
