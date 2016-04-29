from django import forms

class VisualForm(forms.Form):
    title = forms.CharField(label='Title')
    douban_id = forms.CharField(label='Douban Id')
    imdb_id = forms.CharField(label='IMDB Id')
    original_title = forms.CharField(label='Original Title')
    year = forms.IntegerField(label='Year')
    rating = forms.FloatField(label='Rating')
    images = forms.CharField(label='Images')
    summary = forms.CharField(label='Summary')