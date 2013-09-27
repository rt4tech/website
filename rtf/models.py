import re
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from geopy import geocoders
from localflavor.us.us_states import US_STATES
from time import sleep


class Protest(models.Model):

    WE_HAVE_IT = 'We have it'
    REQUESTED = 'Requested'
    UNREQUESTED = 'Unrequested'
    REQUEST_STATUSES = (
        (WE_HAVE_IT, 'We have it'),
        (REQUESTED, 'Requested'),
        (UNREQUESTED, 'Unrequested'),
    )

    confirmed = models.BooleanField(default=False,blank=True)
    state = models.CharField(max_length=255,null=True,blank=True)
    city = models.CharField(max_length=255,null=True,blank=True)
    location = models.CharField(max_length=255,null=True,blank=True)
    date = models.DateField(default=timezone.now,editable=True, null=True,blank=True)
    contact_info_status = models.CharField(max_length=50,
                        choices=REQUEST_STATUSES,
                        default=UNREQUESTED, null=True,blank=True)
    time= models.CharField('Time', max_length=255,null=True,blank=True)
    organizer = models.CharField(max_length=255,null=True,blank=True)
    permit_status = models.CharField(max_length=255,null=True,blank=True)
    reddit_page = models.CharField(max_length=255,null=True,blank=True)
    fb_page = models.CharField(max_length=255,null=True,blank=True)
    twitter = models.CharField(max_length=255,null=True,blank=True)
    other = models.TextField(max_length=2000,null=True,blank=True)
    latitude = models.FloatField(editable=False,default=0.0)
    longitude = models.FloatField(editable=False,default=0.0)
    state_slug = models.CharField(max_length=255, default=None, blank=True, editable=False)
    city_slug = models.CharField(max_length=255, default=None, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if self.state is not None:
            self.state_slug = slugify(self.state)
        if self.city is not None:
            self.city_slug = slugify(self.city)
        super(Protest, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"{0}, {1}".format(self.state, self.city)

    def generateLatLong(self):
        if self.latitude == 0.0 or self.longitude == 0.0:
            g = geocoders.GoogleV3()
            if self.city == None:
                place, (lat, lng) = g.geocode("{0}".format(self.state), exactly_one=False)[0]
            else:
                place, (lat, lng) = g.geocode("{0} {1}".format(self.state, self.city), exactly_one=False)[0]
            self.latitude = lat
            self.longitude = lng
            sleep(.5)

    def get_absolute_url(self):
        if self.city is None:
            return u"/protests/{0}/".format(self.state_slug)
        return "/protests/{0}/{1}/".format(self.state_slug, self.city_slug)

    def to_json(self):
        return {
            'state': self.state,
            'city': self.city or 'N/A',
            'date': self.date.strftime("%Y-%m-%d") if self.date else 'TBA',
            'url': self.get_absolute_url(),
            'latitude': self.latitude,
            'longitude': self.longitude
        }


class Volunteer(models.Model):
    email = models.EmailField(max_length=255, blank=False, null=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    city = models.CharField(max_length=255, blank=False, null=False)
    state = models.CharField(max_length=2, blank=True, null=True, choices=US_STATES, help_text="US State if you're in the US")
    phone = models.CharField(max_length=10, blank=True, null=True, help_text="Numbers only")
    communications = models.NullBooleanField(help_text="PR, Social Media, Communications")
    design = models.NullBooleanField(help_text="Graphic Design for Print, Web, and other Media")
    development = models.NullBooleanField(help_text="Frontend and backend development")
    multimedia = models.NullBooleanField(help_text="Audio/Video skills")
    organizing = models.NullBooleanField(help_text="Local chapter organizing")
    events = models.NullBooleanField(help_text="National event organizing")
    signup_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    contacted = models.BooleanField(default=False)
    contact_date = models.DateTimeField(null=True, blank=True)
    contacted_by = models.ForeignKey(User, null=True, blank=True)

    other = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        # clean non-numeric characters from phone field
        if self.phone is not None:
            self.phone = re.compile(r'[^\d]+').sub('', self.phone)
        super(Volunteer, self).save(*args, **kwargs)


class Chapter(models.Model):
    city = models.CharField(max_length=255, blank=False, null=False)
    state = models.CharField(max_length=2, blank=True, null=True, choices=US_STATES, help_text="US State if chapter is in the US")
    latitude = models.FloatField(editable=False,default=0.0)
    longitude = models.FloatField(editable=False,default=0.0)
    organizer = models.CharField("Local Organizer", max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    facebook = models.URLField(max_length=255, null=True, blank=True)
    twitter = models.URLField(max_length=255, null=True, blank=True)
    website = models.URLField(max_length=255, null=True, blank=True)
    other = models.URLField("Other URL", max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    info = models.TextField("Additional Info", blank=True, null=True)
    state_slug = models.CharField(max_length=255, default=None, blank=True, editable=False)
    city_slug = models.CharField(max_length=255, default=None, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if self.state is not None:
            self.state_slug = slugify(self.state)
        if self.city is not None:
            self.city_slug = slugify(self.city)
        super(Chapter, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"{0}, {1}".format(self.city, self.state)

    def generateLatLong(self):
        if self.latitude == 0.0 or self.longitude == 0.0:
            g = geocoders.GoogleV3()
            if self.city == None:
                place, (lat, lng) = g.geocode("{0}".format(self.state), exactly_one=False)[0]
            else:
                place, (lat, lng) = g.geocode("{0} {1}".format(self.state, self.city), exactly_one=False)[0]
            self.latitude = lat
            self.longitude = lng
            sleep(.5)

    def get_absolute_url(self):
        if self.city is None:
            return u"/chapters/{0}/".format(self.state_slug)
        return "/chapters/{0}/{1}/".format(self.state_slug, self.city_slug)

    def to_json(self):
        return {
            'state': self.state,
            'city': self.city or 'N/A',
            'url': self.get_absolute_url(),
            'latitude': self.latitude,
            'longitude': self.longitude
        }


# Signal handling
@receiver(pre_save)
def pop_latlong(sender, instance, *args, **kwargs):
    if sender in [Protest, Chapter]:
        instance.generateLatLong()
