from django import forms
from .models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'price', 'image', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
 from django import forms
from .models import Category, Subcategory

class SearchForm(forms.Form):
    keywords = forms.CharField(label='Keywords', max_length=100, required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='All Categories', required=False)
    subcategory = forms.ModelChoiceField(queryset=Subcategory.objects.all(), empty_label='All Subcategories', required=False)
