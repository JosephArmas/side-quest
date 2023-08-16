import bcrypt as bcrypt


class GenerateHash:
    @staticmethod
    def create_salt():
        return bcrypt.gensalt().decode('utf-8')

    @staticmethod
    def create_hash(password, salt):
        return bcrypt.hashpw(password.encode('utf-8'), salt.encode('utf-8')).decode('utf-8')


