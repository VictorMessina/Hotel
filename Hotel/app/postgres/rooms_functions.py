from app.models import Room


def find_all_room_data(id_room):
    room_data = Room.objects.select_related("fk_room_info").get(room_id = id_room)
    return room_data
