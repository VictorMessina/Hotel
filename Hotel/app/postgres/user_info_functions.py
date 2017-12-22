from app.models import UserInfo
from app.postgres import user_type_functions


def create_user_info(first_name, last_name, email, telephone, cellphone, gender, birthday, identification_number):
    try:
        user_type = user_type_functions.find_user_type_by_identification_number(identification_number)
        user_info = UserInfo(first_name = first_name, last_name = last_name, email = email, telephone = telephone, cellphone = cellphone, gender = gender, birthday = birthday, fk_user_type_id = user_type.user_type_id).save()
        return user_info
    except UserInfo.DoesNotExist:
        print('user info not registered')
        return None


def update_first_name(first_name, user_id):
    try:
        user_info = UserInfo.objects.get(user_info_id = user_id)
        user_info.first_name = first_name
        user_info.save()
        return True
    except UserInfo.DoesNotExist:
        print("first name not updated")
        return None


def update_last_name(last_name, user_id):
    try:
        user_info = UserInfo.objects.get(user_info_id = user_id)
        user_info.last_name = last_name
        user_info.save()
        return True
    except UserInfo.DoesNotExist:
        print("last name not updated")
        return None


def update_email(email, user_id):
    try:
        user_info = UserInfo.objects.get(user_info_id = user_id)
        user_info.email = email
        user_info.save()
        return True
    except UserInfo.DoesNotExist:
        print("e-mail not updated")
        return None


def update_telephone(telephone, user_id):
    try:
        user_info = UserInfo.objects.get(user_info_id = user_id)
        user_info.telephone = telephone
        user_info.save()
        return True
    except UserInfo.DoesNotExist:
        print("telephone not updated")
        return None


def update_cellphone(cellphone, user_id):
    try:
        user_info = UserInfo.objects.get(user_info_id = user_id)
        user_info.cellphone = cellphone
        user_info.save()
        return True
    except UserInfo.DoesNotExist:
        print("cellphone not updated")
        return None


def update_gender(gender, user_id):
    try:
        user_info = UserInfo.objects.get(user_info_id = user_id)
        user_info.gender = gender
        user_info.save()
        return True
    except UserInfo.DoesNotExist:
        print("gender not updated")
        return None


def update_birthday(birthday, user_id):
    try:
        user_info = UserInfo.objects.get(user_info_id = user_id)
        user_info.birthday = birthday
        user_info.save()
        return True
    except UserInfo.DoesNotExist:
        print("birthday not updated")
        return None
