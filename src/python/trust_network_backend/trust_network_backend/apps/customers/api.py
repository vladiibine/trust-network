from tornado import gen

from restless.preparers import FieldsPreparer

from contrib.handlers import RestHandler

from contrib.db import session
from contrib.db.utils import get_or_404

from .models import Customer


class CustomerHandler(RestHandler):
    model = Customer
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name',
        'created_at': 'created_at'
    })

    @gen.coroutine
    def list(self):
        return session.query(Customer).slice(0, 10)

    @gen.coroutine
    def detail(self, id):
        return get_or_404(self.model, id)
