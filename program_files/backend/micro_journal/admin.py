from django.contrib import admin
from django_mongoengine import mongo_admin as admin
from models import JournalEntry

# Register your models here.
# Models from mongoengine can NOT be imported here. Would need to be django Model class.

@admin.register(JournalEntry)
class JournalEntryAdmin(admin.DocumentAdmin):
    pass