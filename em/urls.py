from django.conf.urls import url
from em import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^album/$', views.album, name = 'album'),
    url(r'^contribute/$', views.contribute, name = 'contribute'),
    url(r'^emergency/$', views.emergency, name = 'emergency'),
    url(r'^emergency_request/$', views.emergency_request, name = 'emergency_request'),
    url(r'^event_main/$', views.event_main, name = 'event_main'),
    url(r'^feedback/$', views.feedback, name = 'feedback'),
    url(r'^friends/$', views.friends, name = 'friends'),
    url(r'^myevent/$', views.myevent, name = 'myevent'),
    url(r'^mytrip/$', views.mytrip, name = 'mytrip'),
    url(r'^plan_event/$', views.plan_event, name = 'plan_event'),
    url(r'^plan_trip/$', views.plan_trip, name = 'plan_trip'),
    url(r'^search_event/$', views.search_event, name = 'search_event'),
    url(r'^search_trip/$', views.search_trip, name = 'search_trip'),
    url(r'^settings/$', views.setting, name = 'setting'),
    url(r'^story/$', views.story, name = 'story'),
    url(r'^timeline/$', views.timeline, name = 'timeline'),
    url(r'^traveller_main/$', views.traveller_main, name = 'traveller_main'),
]