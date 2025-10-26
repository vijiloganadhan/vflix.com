from django.contrib import admin
from .models import Category,Videos,Seasons,Episodes

# Register your models here.
admin.site.register(Category)
admin.site.register(Videos)
admin.site.register(Seasons)
admin.site.register(Episodes)
