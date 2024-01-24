from django.urls import path, re_path
from django.views.generic import RedirectView, TemplateView

from wiki import views

urlpatterns = [

	path('', views.wiki_index, {'cat': "index",}, name='wiki_index'),

	re_path(r'cat/(?P<cat>[a-zA-Z0-9_.,-]+)$', views.wiki_index, name='wiki_cat'),
	re_path(r'category/(?P<cat>[a-zA-Z0-9_.,-]+)/$', RedirectView.as_view(url='/blog/cat/%(bcat)s')),

	re_path(r'tag/(?P<cat>[a-zA-Z0-9_.,-]+)$', views.wiki_index, name='wiki_tag'),
	re_path(r'tag/(?P<cat>[a-zA-Z0-9_.,-]+)/$', views.wiki_index, name='wiki_tag_ext'),

	re_path(r'(?P<art>[a-zA-Z0-9_.,-]+)$', views.wiki_play, name='wiki_play'),
	re_path(r'(?P<art>[a-zA-Z0-9_.,-]+)/$', views.wiki_play, name='wiki_play_ext'),

	
]
