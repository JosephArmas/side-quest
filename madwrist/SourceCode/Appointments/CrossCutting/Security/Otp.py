import os
import time
import pyotp
from dotenv import load_dotenv
class Otp:
    def get_otp(self):
        load_dotenv()
        key = os.getenv("KEY_OTP")
        otp = pyotp.TOTP(key).now()
        return otp

