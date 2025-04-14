from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('image_url', 'thumbnail')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating is not None:
            if rating < 1:
                raise forms.ValidationError('Rating must be at least 1')
            if rating > 10:
                raise forms.ValidationError('Rating cannot be more than 10')
        return rating
