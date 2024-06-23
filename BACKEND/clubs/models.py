from users.models import User, BaseModel
from peewee import *



class Club(BaseModel):
    id = CharField(primary_key=True)
    name = CharField()
    type = CharField(null=True)
    description = TextField(null=True)

class ClubMember(BaseModel):
    user = ForeignKeyField(User, backref='memberships')
    club = ForeignKeyField(Club, backref='members')