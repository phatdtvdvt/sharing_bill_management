from users.models import User, BaseModel
from bills.models import Bill
from peewee import *

STATUS = [
    ("pending", "Opening"),
    ("waiting", "Closed"),
    ("finish", "Finish")
]



class Transaction(BaseModel):
    id = CharField(primary_key=True)
    user = ForeignKeyField(User, backref='transactions')
    bill = ForeignKeyField(Bill, backref='transactions')
    paid_amount = IntegerField(default=0)
    payment_status = CharField(choices= STATUS, default='Pending')
    additional_info = CharField(null=True)