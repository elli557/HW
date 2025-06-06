from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

GENDER = (
        ('male', 'male'),
        ('female', 'female'),
    )

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Укажите email')
    phone_number = forms.CharField(required=True, label='Укажите номер телефона')
    age = forms.IntegerField(required=True, label='Укажите возраст')
    gender = forms.ChoiceField(choices=GENDER, required=True)
    experience = forms.IntegerField(required=True, label='Укажите стаж работы')

    class Meta:
        model = models.CustomUser
        fields  = (
            'username', 
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'gender',
            'phone_number',
            'experience',
        )
        
    def save(self, commit = True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.age = self.cleaned_data['age']
        user.gender = self.cleaned_data['gender']
        user.experience = self.cleaned_data['experience']

        if commit:
            user.save()
        return user