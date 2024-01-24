from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from wiki.models import *

def bt_w_publier(modeladmin, request, queryset):
	queryset.update(w_publier=True)
bt_w_publier.short_description = "Passer en Public"
def bt_w_not_publier(modeladmin, request, queryset):
	queryset.update(w_publier=False)
bt_w_not_publier.short_description = "Passer en Priver"

class Wiki_Admin(ImportExportModelAdmin):
	form = Wiki_Admin_Form
	list_display = ('w_titre', 'w_description', 'w_publier','w_publdate','w_reading')
	list_filter = ('w_publier','w_cat','w_publdate')
	exclude = ('w_publier','w_reading',)
	filter_horizontal = ('w_cat',)
	actions = [bt_w_publier, bt_w_not_publier]
	search_fields = ['w_titre','w_contenu']

admin.site.register(Wiki, Wiki_Admin)

class Cat_Wiki_Admin(admin.ModelAdmin):
	list_display = ('cw_titre', 'cw_titre_slgify')
	pass
admin.site.register(Cat_Wiki, Cat_Wiki_Admin)


