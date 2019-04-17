from django.contrib import admin

# Register your models here.

from idp_app.models import Country, SituationType, Year, FocalPoint, AidProvider, Situation

# Register your models here.

admin.site.register(Situation)

admin.site.register(Country)

admin.site.register(SituationType)

admin.site.register(Year)

admin.site.register(FocalPoint)

admin.site.register(AidProvider)
