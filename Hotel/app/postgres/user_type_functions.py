from app.models import UserType
from app.postgres import nationality_functions

def create_user_type(identification_number, resident, last_address, nationality_id):
    try:
        _nationality_id = nationality_functions.find_nationality_by_id(nationality_id)
        user_type = UserType(identification_number = identification_number, resident = resident, last_address = last_address, fk_nationality_id = _nationality_id.nationality_id).save()
        return user_type
    except Exception:
        print("Is not possible create user type")
        return None


def find_user_type_by_identification_number(identification_number):
    try:
        user_type = UserType.objects.get(identification_number = identification_number)
        return user_type
    except UserType.DoesNotExist:
        print("user type not exist")
        return None
