from django.contrib import admin

from .models import Sponsor, Ticker, Update

# Register your models here.
admin.site.register(Sponsor)
admin.site.register(Ticker)
admin.site.register(Update)
