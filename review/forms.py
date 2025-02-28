from django import forms

class CodeReviewForm(forms.Form):
    rating = forms.IntegerField(min_value=1, max_value=5)

class CommentForm(forms.Form):
    text = forms.TextField()