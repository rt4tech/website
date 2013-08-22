from django.contrib import admin
from rtf.models import Protest, Volunteer

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'city', 'state', 'organizing', 'communications', 'design', 'development', 'multimedia')
    list_filter = ('state', 'organizing', 'communications', 'design', 'development', 'multimedia')

admin.site.register(Protest)
admin.site.register(Volunteer, VolunteerAdmin)
