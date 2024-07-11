#!/usr/bin/env python3
'''encrypting passwords'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''returns byte string password'''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''implement is_valid to validate provided password
    matched hashed_password
    '''
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
