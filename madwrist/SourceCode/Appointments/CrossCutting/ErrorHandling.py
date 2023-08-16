from CrossCutting.Response import Response
import validate_email


class ErrorHandling:
    def is_valid_password(self, password):
        response = Response()
        valid_strings: set = {'@', '$', '!', '.', '-'}
        if len(password) < 8:
            response.message = "Password must be greater than 8"
            return response
        for i in range(len(password)):
            if password[i] == " ":
                response.message = "No spaces. Enter new password"
                return response
            if not password[i].isalpha() and not password[i].isnumeric() and password[i] not in valid_strings:
                response.message = "Invalid Password. Allowed characters: (@, !, $, ., -)"
                return response
        response.message = "Valid Password"
        response.is_successful = True
        return response

    def is_valid_email(self, email):
        response = Response()
        is_valid = validate_email.validate_email(email)
        if not is_valid:
            response.message = "Not a valid email"
            return response
        response.message = "Valid email"
        response.is_successful = True
        return response


