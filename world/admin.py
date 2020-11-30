from django.contrib.gis import admin
from .models import WorldBorder,Post

admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(Post)
