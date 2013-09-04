
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rtf import views

from mezzanine.core.views import direct_to_template


admin.autodiscover()

# Add the urlpatterns for any custom Django applications here.
# You can also change the ``home`` view to add your own functionality
# to the project's homepage.

urlpatterns = patterns("",

    # Protest pages
    url("^protests/$", views.protests, name="protests"),
    url("^protests/(?P<protest_id>\d+)/$", views.protest_by_id, name="protest_by_id"),
    # url("^protests/(?P<state>[-\w]+)/$", views.protests_by_state, name="protests_by_state"),
    url("^protests/(?P<state>[-\w]+)/(?P<city>[-\w]+)/$", views.protest_by_city, name="protest_by_city"),
    url("^protests/recalclatlong/", views.protest_lat_long, name="protests_lat_long"),
    url("^protests.json/$", views.protests_json, name="protests_json"),

    # Chapter pages
    url("^chapters/$", views.chapters, name="chapters"),
    # url("^chapters/(?P<state>[-\w]+)/$", views.chapters_by_state, name="chapter_by_state"),
    url("^chapters/(?P<state>[-\w]+)/(?P<city>[-\w]+)/$", views.chapter_by_city, name="chapter_by_city"),
    url("^chapters/recalclatlong/", views.chapter_lat_long, name="chapters_lat_long"),
    url("^chapters.json/$", views.chapters_json, name="chapters_json"),

    # Forms
    url("^volunteer/$", views.volunteer, name="volunteer"),
    url("^thanks/$", direct_to_template, {'template': 'forms/thanks.html'}, name="thanks"),

    # Change the admin prefix here to use an alternate URL for the
    # admin interface, which would be marginally more secure.
    ("^admin/", include(admin.site.urls)),

	# just parking the map somewhere for now to see it reply
	url("^map/", direct_to_template, {"template": "map.html"}, name="map"),

	#blitz.io testing
	url("^mu-8fe3bdc8-01cc3afb-cb5e87cd-be5e45d7", views.blitzio, name="blitzio"),

    # Mezzanine URLs
    url("^$", direct_to_template, {"template": "index.html"}, name="home")
)

urlpatterns += patterns("", ("^", include("mezzanine.urls")))

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
