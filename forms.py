from django import forms
from tinymce.widgets import TinyMCE
from wiki.models import Wiki

class Wiki_Admin_Form(forms.ModelForm):
    w_description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))
    w_contenu = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    w_right = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Wiki
        fields = '__all__'