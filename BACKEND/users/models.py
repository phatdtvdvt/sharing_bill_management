from peewee import *





class BaseModel(Model):
    class Meta:
        database = 

class User(BaseModel):
    id = CharField(primary_key=True)
    email = CharField(unique=True)
    name = CharField()
    nickname = CharField(null=True)
    avatar = CharField(null=True)
    bank_name = CharField()
    bank_id = CharField()
    is_admin = BooleanField(default=False)
    first_login = BooleanField(default=True)