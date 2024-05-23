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
    email = fields.Email()
    name = fields.Str()
    created_at = fields.Date()
    message = fields.Str()