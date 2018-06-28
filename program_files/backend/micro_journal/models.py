from mongoengine import *

connect("microj")


class JournalEntry(Document):
    created_timestamp = DateTimeField(required=True)
    updated_timestamp = DateTimeField(required=True)
    user_id = StringField(max_length=25, required=True)
    day_number = IntField(required=True)
    memento = StringField(max_length=120, required=False)
    to_do = ListField(required=False)
    gratitude = ListField(required=False)
    other_comments = StringField(required=False)
    sleep = DictField(required=False)
    activities = DictField(required=False)
    goals = ListField(required=False)
    meta = {'collection': 'JournalEntries'}
