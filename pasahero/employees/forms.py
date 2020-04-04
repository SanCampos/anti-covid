from django import forms
from django.forms import formset_factory

from .times import TIME_OPTIONS_FOR_EMPLOYEES
from transportations.models import Routes, Directions, Times

class CreateDirectionForm(forms.ModelForm):
    class Meta:
        model = Directions
        fields = ('start_location', 'end_location', 'vehicle', 'duration_minutes')

class CreateRouteForm(forms.ModelForm):
    class Meta:
        model = Routes
        fields = ('name', 'via', 'point_a', 'point_b')
        labels = {
            "name":"Route Name",
            "point_a":"Point A",
            "point_b":"Point B",
        }

    def __init__(self, *args, **kwargs):
        super(CreateRouteForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Quezon City Circle - Araneta Avenue'
        self.fields['via'].widget.attrs['placeholder'] = 'Quezon Avenue'
        self.fields['point_a'].widget.attrs['placeholder'] = 'Quezon City Circle'
        self.fields['point_b'].widget.attrs['placeholder'] = 'Araneta Avenue'

class CreateDirectionForm(forms.ModelForm):
    class Meta:
        model = Directions
        fields = ('start_location', 'end_location', 'vehicle', 'duration_minutes')

class CreateTimesForm(forms.ModelForm):
    class Meta:
        model = Times
        fields = ('time', 'capacity')
        widgets = {'time': forms.DateInput(attrs={'class':'form-control', 'type':'time'}),
        }

CreateTimeFormSet = formset_factory(CreateTimesForm, extra=4, min_num=1)