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
