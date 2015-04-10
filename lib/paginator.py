# -*-coding: utf-8-*-

__author__ = 'wangyu'

from math import ceil


class Paginator(object):
    def __init__(self, query, page=1, per_page=5, object=None, count=None):
        self.query = query
        self.page = page
        self.per_page = per_page
        self._count = count
        self._object = object

    @property
    def count(self):
        if self._count is None:
            self._count = self.query.count()
        return self._count

    @property
    def total_pages(self):
        return int(ceil(self.count * 1.0 / self.per_page))

    def has_next(self):
        return self.page < self.total_pages

    def has_previous(self):
        return self.page > 1

    def paginate(self):
        if self._object is None:
            self._object = self.query.paginate(self.page, self.per_page)
        return self._object