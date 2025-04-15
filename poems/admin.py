from django.contrib import admin

from .models import Poem
from .models import Review

# Register your models here.
admin.site.register(Poem)
admin.site.register(Review)
