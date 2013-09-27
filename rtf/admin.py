from django.contrib import admin
from rtf.models import Protest, Volunteer, Chapter

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'city', 'state', 'organizing', 'communications', 'design', 'development', 'multimedia', 'signup_date', 'contacted', 'contacted_by')
    list_filter = ('state', 'organizing', 'communications', 'design', 'development', 'multimedia', 'signup_date', 'contacted')

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('city', 'state', 'email', 'website', 'organizer', 'facebook', 'twitter')
    list_filter = ('state',)

admin.site.register(Protest)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Chapter, ChapterAdmin)
