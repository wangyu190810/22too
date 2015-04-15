# -*-coding: utf-8-*-

__author__ = 'wangyu'

from random import choice
from string import ascii_letters


def random_string(length=8, letters=ascii_letters):
    return ''.join(choice(letters) for _ in range(length))
