import sys
from django.apps import AppConfig


class WikiConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'wiki'
	
	def ready(self):

		if 'migrate' in sys.argv:
			return
		
		print("-- Démarage du Wiki --")
		print(">> Vérification des variables d'environement")

		from core.models import Page
		try :
			page = Page.objects.get(p_titre_slugify = "wiki")
		except :
			page = Page()

		page.p_titre = "Wiki"
		page.p_icone = "fas fa-book-dead"
		page.p_adresse = "/wiki/"
		page.p_menu_position = "haut"
		page.p_type = "sys"
		page.p_menu_poid = 30

		page.save()
