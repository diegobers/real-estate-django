from django import forms

from products.models import Casa


class SearchCasaForm(forms.ModelForm): 
    
    class Meta:
        model = Casa
        fields = ["id", "category", "city", "price"]


