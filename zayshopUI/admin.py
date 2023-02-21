from django.contrib import admin
from .models import Prodct,Color,Size,ContactUsForm
# Register your models here.

admin.site.register(Prodct)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(ContactUsForm)