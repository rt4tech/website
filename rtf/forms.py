from django import forms
from localflavor.us.forms import USStateSelect
from rtf.models import Volunteer

class VolunteerForm(forms.ModelForm):

    class Meta:
        model = Volunteer
        fields = ('name',
                  'email',
                  'phone',
                  'city',
                  'state',
                  'organizing',
                  'communications',
                  'design',
                  'development',
                  'multimedia',
                  'other')
        widgets = {
            'name': forms.TextInput(attrs={'class':'input-xlarge'}),
            'email': forms.TextInput(attrs={'class':'input-xlarge'}),
            'phone': forms.TextInput(attrs={'class':'input-xlarge'}),
            'city': forms.TextInput(attrs={'class':'input-xlarge'}),
            'state': USStateSelect,
            'communications': forms.CheckboxInput,
            'design': forms.CheckboxInput,
            'development': forms.CheckboxInput,
            'multimedia': forms.CheckboxInput,
            'organizing': forms.CheckboxInput
        }
