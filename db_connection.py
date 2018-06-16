import pymongo
import datetime


def db_connect():
    try:
        connection = pymongo.MongoClient('localhost', 27017)
        print("Connected successfully to database")
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to the database: %s", str(e))
    return connection


def create_journal_entry():
    db.JournalEntries.insert({"created_at": datetime.datetime.now(datetime.timezone.utc),
                              "user_id": str(db.Users.find_one()["_id"])})  # TODO make sure this dynamically takes user


def update_journal_entry(journal_entry_id, **kwargs):
    try:
        db.update({"_id": journal_entry_id}, {"$set": {**kwargs}})
    except:  # TODO specify error(s) narrower
        print("Unable to update journal entry: " + str(journal_entry_id))


connection = db_connect()
if connection:
    db = connection.microj

create_journal_entry(db)

print(str(db.Users.find_one()["screen_name"]))
