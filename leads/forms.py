from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Lead, Book


User = get_user_model()

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name', 'last_name', 'age', 'id_number', 'physical_address', 'postal_address', 'gender', 'agent'
        )


class BookForm(forms.ModelForm):
    class Meta: 
        model = Book
        fields = (
            'name','surname','bank_statement', 'id_copy', 'proof_residence', 'water_proof', 'electricity_proof', 'sworn_affidavit' 
        )


class LeadForm(forms.Form):
      first_name = forms.CharField()
      last_name = forms.CharField()
      age = forms.IntegerField(min_value=20)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'category',
        )