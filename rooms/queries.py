# from strawberry.types import Info
from . import models


def get_all_rooms():
    # if info.context.request.user.is_authenticated:
    return models.Room.objects.all()


# else:
# raise Exception("Not aut.")


def get_room(pk: int):
    try:
        return models.Room.objects.get(pk=pk)
    except models.Room.DoesNotExist:
        return None
