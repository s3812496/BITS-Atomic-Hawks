from django.contrib import admin

# Register your models here.

from .models import Song
admin.site.register(Song)

from .models import Album
admin.site.register(Album)

from .models import Artist
admin.site.register(Artist)

from .models import Contact
admin.site.register(Contact)