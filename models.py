from django.db import models
from django import forms

from django.template.defaultfilters import slugify

from trumbowyg.widgets import TrumbowygWidget

class Cat_Wiki(models.Model) :
	cw_titre = models.CharField("Titre", max_length = 128, unique = True)
	cw_titre_slgify = models.CharField("Titre Slugify", max_length = 128, blank = True, editable = False)

	class Meta :
		verbose_name = 'Catégories'
		verbose_name_plural = 'Catégories'

	def save(self, *args, **kwargs) :
		self.cw_titre_slgify = slugify(self.cw_titre)
		super(Cat_Wiki, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.cw_titre
	def __str__(self):
		return '%s' % (self.cw_titre)

class Wiki(models.Model) : #Architecture pour le Wiki
	w_titre = models.CharField("Titre", max_length = 128, unique = True)
	w_titre_slugify = models.CharField("Titre Slugify", max_length = 128, blank = True, editable = False)
	w_cat = models.ManyToManyField(Cat_Wiki, verbose_name="Catégories" , blank = True)
	w_description = models.TextField("Résumé", blank = True)
	w_contenu = models.TextField("Contenu", blank = True)
	w_right = models.TextField("Contenu à droite", blank = True)
	w_publier = models.BooleanField("Publié", default = False)
	w_reading = models.IntegerField("Nb Lectures", default = 0)
	w_publdate = models.DateTimeField("Mise à jour le", auto_now_add=True)

	class Meta :
		verbose_name = 'Gestion du Wiki'
		verbose_name_plural = 'Gestion du Wiki'
		ordering = ['w_titre']

	def save(self, *args, **kwargs) :
		self.w_titre_slugify = slugify(self.w_titre)
		super(Wiki, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.w_titre
	def __str__(self):
		return '%s' % (self.w_titre)

class Wiki_search_Form(forms.Form):
	w_search = forms.CharField(label='Vous recherchez un page ?', max_length=100)

class Wiki_Admin_Form(forms.ModelForm):
	class Meta:
		model = Wiki
		exclude = ['w_titre_slugify','w_reading']
		widgets = {
			'w_contenu': TrumbowygWidget(attrs={'rows':4, 'cols':15}),
			'w_right': TrumbowygWidget(attrs={'rows':4, 'cols':15}),
			}