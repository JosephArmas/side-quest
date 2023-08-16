from Managers.RegisterManager.RegisterManager import RegisterManager
from Services.RegisterService.RegisterService import RegisterService

if __name__ == "__main__":
    email = input('Enter email: ')
    password = input('Enter password: ')
    r_service = RegisterService("DEV_SQL_USER")
    r_manager = RegisterManager(r_service)
    r_manager.create_user(email, password)


