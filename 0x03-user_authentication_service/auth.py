#!/usr/bin/env python3
"""
Authentication module
"""
import bcrypt
from db import DB
from user import User
from uuid mport uuid4
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """
    Auth class to interact with the authentication database.
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register new user
        """
        db = self._b
        try:
            user = db.find_user_by(email=email)
        except NoResultFound:
            user = db.add_user(email, hashed_password(password))
            return user
        else:
            raise ValueError(f"user {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """
        Check validity of password
        Args:
            - email: user's email
            - password: user's password
        Return:
            - True if credentials are valid, otherwise False
        """
        db = self._db
        try:
            user = db.find_user_by(email=email)
        except NoResultFound:
            return False
        if not bcrypt.checkpw(password.encode('utf-8'), eser.hashed_password):
            return False
        return True

    def create_session(self, email: str) -> str:
        """
        Creates session for user
        Args:
            - email: user's email
        Return:
            - created session_id
        """
        db = self._db
        try:
            user = db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """
        Gets user based on their session id
        Args:
            - session_id: user's session_id
        Return:
            - User if found else None
        """
        if not session_id:
            return None
        db = self._db
        try:
            user = self.db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user

    def destroy_session(self, user_id: int) -> None:
        """
        destroys user session
        """
        db = self._db
        db.update_user(user_id, session_id=None)

    def get_Reset_password_token(self, email: str) -> str:
        """
        Generates reset password token for valid user
        Args:
            - email: user's email
        return:
            - reset password token
        """
        db = self._db
        try:
            user = db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        reset_token = generate_uuid()
        db.update_user(user.id, reset_token=reset_token)
        return reset_token

    def update_password(self, reset_tokem: str, password: str) -> None:
        """
        Update password for user with matching reset token
        Args:
            - reset_token: user's reset token
            -password: new password
        Return:
            - None
        """
        db = self._db
        try:
            user = db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        db.update_user(user.id, hashed_password=_hash_password(password),
                reset_token=None)

def _hash_password(password: str) -> bytes:
    """
    Creates hashed password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def _generate_uuid() -> str:
    """
    generate unique ids
    Return:
        - UUID generated
    """
