# File Name: utils.py
# Author: Jesse Malinen
# Description: utility script for hashing

from passlib.hash import pbkdf2_sha256

def hash_password(password):
    return pbkdf2_sha256.hash(password)

def check_password(password, hashed):
    return pbkdf2_sha256.verify(password, hashed)