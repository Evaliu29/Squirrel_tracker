from django.forms import ModelForm

from .models import Squirrel

class SquirrelForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = [
            'Latitude',
            'Longitude',
            'Unique_Squirrel_ID',
            'Shift',
            'Date',
            'Age'
                ]

