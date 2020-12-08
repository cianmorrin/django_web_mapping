from django.contrib.gis import admin
from .models import WorldBorder,Post,Flight

admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(Post)
admin.site.register(Flight)