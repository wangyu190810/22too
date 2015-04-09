# -*-coding: utf-8-*-

__author__ = 'wangyu'

import hashlib

from sqlalchemy import Column, String, Integer

from .base import Base
from lib.utils import random_string


class User(Base):
    __tablename__ = "bloguser"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(80))

    password_hash = Column(String(64))
    password_salt = Column(String(8), default=lambda: random_string(8))

    @classmethod
    def create_user(cls, connection, username, password):
        user = User(username=username)
        user.set_password(password)
        connection.add(user)
        connection.commit()

    @classmethod
    def check_user(cls, connection, username, password):
        try:
            user = connection.query(User).filter_by(username=username)
            if user.encrypt_password(password) != user.password_hash:
                user = None
        except cls.DoesNotExist:
            user = None
        return connection.execute(user).scalar()

    def encrypt_password(self, password, salt=None):
        if not salt:
            salt = self.password_salt or self.regenerate_salt()
        return hashlib.sha256('%s - %s' % (password, salt)).hexdigest()

    def regenerate_salt(self):
        self.password_salt = random_string(8)
        return self.password_salt

    def set_password(self, password):
        self.password_hash = self.encrypt_password(password)

    def verify_password(self, password):
        return self.encrypt_password(password) == self.password_hash