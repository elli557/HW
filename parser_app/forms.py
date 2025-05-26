from django import forms
from . import models, parser_kinob

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('kinob.net', 'kinob.net'),
    
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]
    
    def parser_data(self):
        if self.data['media_type'] == 'kinob.net':
            kinob_films = parser_kinob.parsing_kinob()
            for i in kinob_films:
                models.Parser_Kinob.objects.create(**i)
