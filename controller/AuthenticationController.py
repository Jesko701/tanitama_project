import jwt
from datetime import datetime, timedelta

class JWT:
    def __init__(self, secret_key, algorithm=['HS256']):
        self.secret_key = secret_key
        self.algorithm = algorithm

    def generateToken(self, payload, expiration_minutes=None):
        if expiration_minutes:
            expiration_time = datetime.now() + timedelta(minutes=expiration_minutes)
            payload['exp'] = expiration_time
        token = jwt.encode(payload, self.secret_key, 'HS256')
        return token
    
    def decode_token(self,token):
        try:
            decoded = jwt.decode(token, self.secret_key, 'HS256')
            return decoded
        except jwt.ExpiredSignatureError:
        # Token has expired
            return None
        
        except jwt.InvalidTokenError:
            # Invalid token
            return None
        
    def debug(self):
        return self.secret_key

