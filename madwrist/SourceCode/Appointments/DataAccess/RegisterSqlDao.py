from DataAccess.Abstractions.ISqlBoiler import ISqlBoiler
from Models.Users import Users


class RegisterSqlDao(ISqlBoiler):
    def __init__(self, url):
        super().__init__(url)

    def insert_user(self, username, password):
        new_user = Users(username=username, password=password)
        return self.add_query(new_user)




