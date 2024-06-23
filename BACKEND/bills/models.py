from users.models import User, BaseModel
from peewee import *


STATUS = [
    ("opening", "Opening"),
    ("closed", "Closed"),
    ("finish", "Finish")
]

TOPIC = [
    ("sport", "Sport"),
    ("entertaiment", "entertaiment"),
    ("eat/drink", "Eat/drink"),
    ("party", "Party")
]

class Bill(BaseModel):
    id = CharField(primary_key=True)
    title = CharField()
    category = CharField(choices= TOPIC, null=True)
    total_amount = IntegerField(default=0)
    created_at = DateTimeField()
    created_by = ForeignKeyField(User, backref='bills')
    updated_by = CharField(null=True)
    additional_info = CharField(null=True)
    status = CharField(choices = STATUS, default="opening")
