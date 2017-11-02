from app.models import UserPrivileges


def find_user_privileges_by_description(description):
    try:
        user_privileges = UserPrivileges.objects.get(description = description)
        return user_privileges
    except UserPrivileges.DoesNotExist:
        print("User privilege not found")
        return None