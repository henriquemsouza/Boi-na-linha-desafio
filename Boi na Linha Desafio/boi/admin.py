from django.contrib import admin
from .models import Mercadoria
from .models import UserProfile




# Register your models here.

admin.site.site_header = 'Boi na Linha Admin'
admin.site.site_title = 'Boi'
admin.site.index_title = 'Administration'


admin.site.register(Mercadoria)

admin.site.register(UserProfile)
