from django import forms
from ratings.models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['beer_name', 'score', 'notes', 'brewer']

  #  def __init__(self, *args, **kwargs):
 #   	super(RatingForm, self).__init__(*args, **kwargs)
#
    #	self.fields['notes'].widget = forms.Textarea()
