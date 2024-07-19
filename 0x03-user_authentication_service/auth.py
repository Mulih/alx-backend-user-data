#!/usr/bin/env python3
"""
Authentication module
"""
import bcrypt
from db import DB

class Auth:
    """
    Auth class to interact with the authentication database.
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exist")
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)

def _hash_password(password: str) -> bytes:
    """
    Creates hashed password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
