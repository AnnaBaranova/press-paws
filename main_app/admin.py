from django.contrib import admin
from .models import Hotel, Room, Profile, Reservation, Pet, Photo

# Register your models here.
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Profile)
admin.site.register(Reservation)
admin.site.register(Pet)
admin.site.register(Photo)
