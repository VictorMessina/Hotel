"""
Definition of models.
"""

from django import forms
from django.db import models

# Create your models here.

class UserPrivileges (models.Model):
    user_privileges_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=20)

class User (models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField("Login", max_length=10)
    password = models.CharField(max_length=64)
    fk_user_privileges = models.ForeignKey(UserPrivileges)

class Nationality (models.Model):
    nationality_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)

class UserType (models.Model):
    user_type_id = models.AutoField(primary_key=True)
    identification_number = models.CharField(max_length=10)
    resident = models.BooleanField()
    last_address = models.CharField(max_length=30)
    fk_nationality = models.ForeignKey(Nationality)

class UserInfo (models.Model):
    user_info_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    telephone = models.CharField(max_length=8)
    cellphone = models.CharField(max_length=10)
    gender = models.CharField(max_length=9)
    birthday = models.DateField()
    fk_user_type = models.ForeignKey(UserType)

class Place (models.Model):
    place_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=10)
    kitchen = models.BooleanField()
    study_room = models.BooleanField()

class RoomSize (models.Model):
    room_size_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=6)

class RoomInfo (models.Model):
    room_info_id = models.AutoField(primary_key=True)
    bathroom_inside = models.BooleanField()
    bath = models.BooleanField()
    double_bed = models.BooleanField()
    study_table = models.BooleanField()
    closet = models.BooleanField()
    tv = models.BooleanField()
    mirror = models.BooleanField()
    nightstand = models.BooleanField()
    fk_room_size = models.ForeignKey(RoomSize)

class Room (models.Model):
    room_id = models.AutoField(primary_key=True)
    door_number = models.IntegerField()
    availability = models.BooleanField()
    share = models.BooleanField()
    fk_room_info = models.ForeignKey(RoomInfo)
    fk_place = models.ForeignKey(Place)