from django.db import models
import uuid
import random
import string
def generate_unique_code():
    length = 20

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break

    return code
class Room(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    code = models.CharField(max_length=300, default=generate_unique_code, unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)        
    def __str__(self):
        return str(code)