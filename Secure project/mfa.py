import pyotp

class MultiFactorAuthentication:
    def __init__(self, secret):
        self.totp = pyotp.TOTP(secret)

    def generate_otp(self):
        return self.totp.now()

    def verify_otp(self, otp):
        return self.totp.verify(otp)
