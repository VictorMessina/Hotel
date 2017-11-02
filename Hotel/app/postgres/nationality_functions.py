from app.models import Nationality


def find_nationality_by_id (nationality_id):
    try:
        natinonality = Nationality.objects.get(nationality_id = nationality_id)
        return natinonality
    except Nationality.DoesNotExist:
        print("Nationality not exist")
        return None