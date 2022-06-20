import time
import string
import secrets
from core.settings import SECRET_KEY
import pytz
from datetime import datetime, timedelta
import jwt
from jwt import ExpiredSignatureError, InvalidSignatureError


TIMEZONE = pytz.timezone("Europe/Moscow")
def generate_charset(length: int):
    return "".join(
        secrets.choice(string.digits + string.ascii_letters) for _ in range(length)
    )

def generate_jwt(user_id, nickname, minutes, count, IsAdmin=0):
    dt = datetime.now() + timedelta(minutes=minutes)
    dt_now = datetime.now()

    token = jwt.encode({
        'token_type': 'access',
        'exp': int(str(time.mktime(dt.timetuple()))[:-2]),
        'iat': dt_now,
        'jti': generate_charset(15),
        'IsAdmin': IsAdmin,
        'count': count,
        'user_id': user_id,
        'nickname': nickname,
    }, SECRET_KEY, algorithm='HS256')

    return {"token": token, "encode": {
        'token_type': 'access',
        'exp': int(str(time.mktime(dt.timetuple()))[:-2]),
        'iat': dt_now,
        'jti': generate_charset(15),
        'IsAdmin': IsAdmin,
        'count': count,
        'user_id': user_id,
        'nickname': nickname,        
    }}

# def read_jwt(token: str):
#     """reads jwt, validates it and return payload if correct"""
#     header_data = jwt.get_unverified_header(token)
#     secret = SECRET_KEY
#     try:
#         payload = jwt.decode(token, key=secret, algorithms=[header_data["alg"]])
#     except ExpiredSignatureError as e:
#         return False
#     except InvalidSignatureError as e:
#         return False
#
#     if "exp" not in payload:
#         return False
#
#     if int(datetime.now(tz=TIMEZONE).timestamp()) > payload["exp"]:
#         return False
#
#     payload.pop("iat", None)
#     payload.pop("exp", None)
#
#     return payload

# print(generate_jwt(user_id=1, nickname="benefix", minutes=10000000, count=20, IsAdmin=1))