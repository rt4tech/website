from django.contrib import admin
from rtf.models import Protest, Volunteer, Chapter

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'city', 'state', 'organizing', 'communications', 'design', 'development', 'multimedia', 'signup_date', 'contacted', 'contacted_by')
    list_filter = ('state', 'organizing', 'communications', 'design', 'development', 'multimedia', 'signup_date', 'contacted', 'contacted_by')
    readonly_fields = ('signup_date', 'contacted_date')

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('city', 'state', 'email', 'website', 'organizer', 'facebook', 'twitter')
    list_filter = ('state',)

class ProtestAdmin(admin.ModelAdmin):
    list_display = ('location', 'date', 'time', 'permit_status', 'confirmed')
    list_filter = ('location', 'date', 'time', 'permit_status', 'confirmed')

admin.site.register(Protest, ProtestAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Chapter, ChapterAdmin)
