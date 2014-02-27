from django import forms
from localflavor.us.forms import USStateSelect
from rtf.models import Volunteer

class VolunteerForm(forms.ModelForm):

    class Meta:
        model = Volunteer
        fields = (
          'name',
          'email',
          'phone',
          'city',
          'state',
          'communications',
          'outreach',
          'operations',
          'legislation',
          'design',
          'development',
          'other')
        widgets = {
            'name': forms.TextInput(attrs={'class':'input-xlarge'}),
            'email': forms.TextInput(attrs={'class':'input-xlarge'}),
            'phone': forms.TextInput(attrs={'class':'input-xlarge'}),
            'city': forms.TextInput(attrs={'class':'input-xlarge'}),
            'state': USStateSelect,
            'communications': forms.CheckboxInput,
            'outreach': forms.CheckboxInput,
            'operations': forms.CheckboxInput,
            'legislation': forms.CheckboxInput,
            'design': forms.CheckboxInput,
            'development': forms.CheckboxInput,
            'events': forms.CheckboxInput
        }
