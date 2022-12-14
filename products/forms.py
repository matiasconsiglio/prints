from django import forms
from .models import Product, Category, ProductSpec


class ProductForm(forms.ModelForm):
    """
    Class form to agregate product fields
    """
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names

        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class SpecForm(forms.ModelForm):
    """
    Class form to agregate product spec fields
    """
    class Meta:
        model = ProductSpec
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
