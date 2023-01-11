from django import forms
from django.db.models import fields 
from productoApp.models import Items,Tag,Marca
class FomularioItem(forms.ModelForm):
    name =forms.CharField(min_length=3, max_length=50)
    price =forms.FloatField(min_value=1, max_value=100000000)
    class Meta:
        model = Items
        fields ='__all__'

class FomularioTag(forms.ModelForm):
    nametag = forms.CharField(min_length=3, max_length=50,)
    class Meta:
        model = Tag
        fields ='__all__'
class FormularioMarca(forms.ModelForm):
    marca = forms.CharField(min_length=3, max_length=50,)
    class Meta:
        model = Marca
        fields ='__all__'
        