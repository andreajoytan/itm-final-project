from django import forms

from .models import Product

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'product_name', 'description', 'price', 'image', 'available')
        
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'product_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'available': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
        
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'description', 'price', 'image', 'available')
        
        widgets = {
            'product_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'available': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES
            }),
        }