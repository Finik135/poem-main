from django import forms

from poems.models import Poem, Review


class CreatePoemForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'style': 'width: 90%; padding: 10px; border: 1px solid #ccc; border-radius: 5px;',
            }
        )
    )

    class Meta:
        model = Poem
        fields = [
            "name",
            "text",
        ]


class CreateReviewPoemForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["text"]
