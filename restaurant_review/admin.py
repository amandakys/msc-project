from django.contrib import admin
from .models import Restaurant, Review, Profile

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(Profile)
