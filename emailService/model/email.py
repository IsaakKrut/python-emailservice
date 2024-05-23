import datetime as dt

from marshmallow import Schema, fields


class Email(object):
    def __init__(self, email, name, message):
        self.email = email
        self.name = name
        self.created_at = dt.datetime.now()
        self.message = message

    def __repr__(self):
        return '<Email(name={self.message!r})>'.format(self=self)


class EmailSchema(Schema):
    email = fields.Str(load_default="defaultEmail@example.com")
    name = fields.Str(load_default="")
    created_at = fields.Date()
    message = fields.Str(load_default="")