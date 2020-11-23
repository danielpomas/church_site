from django.forms import ModelForm, HiddenInput

from churches.models import Person


class SpeakerCreateForm(ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'second_last_name', 'gender', 'is_speaker', 'street_address', 'city',
                  'state', 'country')
