from django import forms
from .validators import MaxSizeFileValidator
from django.forms import ValidationError
from .models import City, Establishment, UserHoisu
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CityForm(forms.ModelForm):

    class Meta:

        model = City
        fields = '__all__'

class EstablishmentForm(forms.ModelForm):
    title = forms.CharField(min_length=3, max_length=50)
    image = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=2)])

    def clean_name(self):
        name = self.cleaned_data["title"]
        exists = Establishment.objects.filter(nombre__iexact=name).exists()

        if exists:
            raise ValidationError("This Establishment already exists")
        return name

    class Meta:
        model = Establishment
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = UserHoisu
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]