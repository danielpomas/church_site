from django.forms import ModelForm, Select

from churches.models import Person
from churches.consts import MaritalStatus


class SpeakerCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SpeakerCreateForm, self).__init__(*args, **kwargs)
        self.fields['is_speaker'].initial = True

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'second_last_name', 'gender', 'marital_status', 'is_speaker', 'street_address', 'city',
                  'state', 'country')
        labels = {
            'marital_status': 'Material Status'
        }
        widgets = {
            'marital_status': Select(choices=MaritalStatus.choices)
        }
