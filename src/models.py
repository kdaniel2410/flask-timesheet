from app import database
from peewee import *


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()


class Shift(BaseModel):
    title = CharField(null=True)
    # user = ForeignKeyField(User, backref="shifts")
    date = DateField()
    income = DecimalField(decimal_places=2)
    expenses = DecimalField(decimal_places=2, null=True)
    reimbursement = DecimalField(decimal_places=2, null=True)
    notes = TextField(null=True)
