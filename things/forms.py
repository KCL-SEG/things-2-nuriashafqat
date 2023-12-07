from things.models import Thing
from django import forms
"""Forms of the project."""

# Create your forms here.
class ThingForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    quantity = forms.IntegerField(widget=forms.NumberInput)

    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']