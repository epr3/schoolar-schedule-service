from functools import wraps
from flask_jwt_extended import get_raw_jwt

def roles_required(roles):
  def decorator_role(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
      jwt_dict = get_raw_jwt()
      if (jwt_dict['context']['role'] not in roles):
        return 'Forbidden', 403
      return fn(*args, **kwargs)
    return wrapper
  return decorator_role
