from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from django.http import HttpResponse, HttpResponseRedirect
from django.utils.html import strip_tags

from django.core.paginator import Paginator

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from django.db.models import Q

#from wiki.forms import *
from core.views import gen_page_base, gen_page_sys
from wiki.models import *

def wiki_index(request, cat):

#print(cat)

	template = loader.get_template('listing.html')
	page = gen_page_base()
	page.p_adresse = reverse('wiki_index')
	page.p_titre = "Les pages du Wiki"
	page.p_contenu = ""
	page.p_right = "Retrouvez les tous les pages sur le wiki"
	page.p_description = strip_tags(page.p_right)
	page.p_mots_clefs = ""
	

	w_search = request.GET.get('w_search')

	if w_search != None:
		page.wiki_search = Wiki_search_Form(initial={'w_search': w_search,})
		q= Q(w_titre__icontains=w_search) | Q(w_mots_clefs__icontains=w_search) | Q(w_description__icontains=w_search)
	else:
		page.wiki_search = Wiki_search_Form()
	if cat == "index":
		if w_search != None:
			wiki_art = Wiki.objects.filter( w_publier = True ).filter(q).order_by( '-w_publdate' )
		else :
			wiki_art = Wiki.objects.filter( w_publier = True ).order_by( '-w_publdate' )
		page.wiki_cat = Cat_Wiki.objects.all()[:15]

	elif cat == "all":
		wiki_art = Wiki.objects.filter( w_publier = True ).order_by( '-w_publdate' )
		page.wiki_cat = Cat_Wiki.objects.all()[:15]
	else :
		if w_search != None:
			wiki_art = Wiki.objects.filter( w_publier = True ).filter( w_cat__cw_titre_slgify = cat ).filter(q).order_by( '-w_publdate' )
		else :
			wiki_art = Wiki.objects.filter( w_publier = True ).filter( w_cat__cw_titre_slgify = cat ).order_by( '-w_publdate' )
		page.wiki_cat = Cat_Wiki.objects.filter( cw_titre_slgify = cat )[:15]
		page.retour = "wiki_index"

	paginator = Paginator(wiki_art, 15)
	page.number = request.GET.get('page')

	page.wiki_art = paginator.get_page(page.number)
	#print(page.wiki_art.paginator.num_pages)
	
	page.wiki_art.nbpage = range(page.wiki_art.paginator.num_pages)

	for cat in page.wiki_cat.all():
		page.p_mots_clefs = page.p_mots_clefs + cat.cw_titre + ', '

	page.wiki_top10 = Wiki.objects.filter( w_publier = True ).order_by( '-w_reading' )[:10]

	html = template.render({
		'page': page,
		'user': request.user,
		}, request)
		
	return HttpResponse(html)

def wiki_play(request, art):

	template = loader.get_template('read.html')
	page = gen_page_base()
	page.p_adresse = reverse('wiki_index')
	page.wiki_art = Wiki.objects.filter(w_titre_slugify = art)[:1]

	for art in page.wiki_art:
		page.p_titre = art.w_titre
		page.p_contenu = art.w_description
		page.p_description = strip_tags(art.w_description)
		if art.w_right != "":
			page.p_right = art.w_right
		else:
			page.p_right = "&nbsp;"

		page.p_mots_clefs = ""
		for cat in art.w_cat.all():
			page.p_mots_clefs = page.p_mots_clefs + cat.cw_titre + ', '

		art.w_reading = art.w_reading + 1
		art.save()

		print(page)

	html = template.render({
		'page': page,
		'user': request.user,
		}, request)
		
	return HttpResponse(html)