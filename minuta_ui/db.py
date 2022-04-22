from importlib.resources import path
import peewee as pw
import os

home_dir = os.path.expanduser("~")
app_home_dir = os.path.join(home_dir, ".minuta")
if os.path.exists(app_home_dir):
    if not os.path.isdir(app_home_dir):
        print("Error!")
else:
    os.makedirs(app_home_dir)

db_uri = os.path.join(app_home_dir, "minuta_projects.db")

db = pw.SqliteDatabase(db_uri)


class Project(pw.Model):
    name = pw.CharField()
    path = pw.CharField()
    status = pw.BooleanField()
    created_date = pw.DateField()

    class Meta:
        database = db


def create_tables():
    with db:
        db.create_tables([Project])
