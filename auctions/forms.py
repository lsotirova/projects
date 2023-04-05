from django.forms import models, NumberInput, HiddenInput, ClearableFileInput, TextInput, Textarea, Select
from django.utils.safestring import mark_safe

from .models import Listing, Bid, Comment


class ListingForm(models.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'category', 'image', 'start_bid']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'style': 'width: 400px', 'placeholder': 'Add a Title'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': 2, 'style': 'width: 800px',
                                           'placeholder': 'Enter Description'}),
            'category': Select(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'image': TextInput(attrs={'class': 'form-control', 'style': 'width: 400px', 'placeholder': 'Enter Image URL'}),
            'start_bid': NumberInput(attrs={'class': 'form-control', 'style': 'width: 400px',
                                            'placeholder': 'Enter Starting Bid Amount'}),
        }

    def clean_image(self):
        image_url = self.cleaned_data.get('image')
        if not image_url:
            image_url = "https://www.yiwubazaar.com/resources/assets/images/default-product.jpg"
        return image_url


class CommentForm(models.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
        widgets = {
            'comment': Textarea(attrs={'class': 'form-control;'})
        }
