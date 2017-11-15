import hashlib
from app.models import User, UserInfo
from app.postgres import user_privileges_functions


def create_user(user_name, password, description):
    encrypted_password = generate_sha256(password)

    try:
        user_privileges = user_privileges_functions.find_user_privileges_by_description(description)
        user = User(user_name = user_name, password = encrypted_password, fk_user_privileges_id = user_privileges.user_privileges_id).save()
        return user
    except Exception:
        print("user not registered")
        return None


def find_all_user_data(user_name):
    try:
        user = User.objects.get(user_name = user_name)
        userInfo = UserInfo.objects.select_related().get(user_info_id = user.user_id)
        data = {'user': user, 'userInfo': userInfo}
        return data
    except  User.DoesNotExist:
        print("User not found")
        return None


def find_user(user_name):
    try:
        user = User.objects.get(user_name = user_name)
        return user
    except  User.DoesNotExist:
        print("User not exist")
        return None


def generate_sha256(password):
    password_hash = hashlib.sha256(str(password).encode('utf-8')).hexdigest()
    return password_hash


def validate_login(user_name, password):
    user_information = find_user(user_name)
    password_hash = generate_sha256(password)
    if user_information is not None:
        if user_information.user_name is not None:
            if user_information.password == password_hash:
                return True
            else:
                return False
    else:
        return False
 
