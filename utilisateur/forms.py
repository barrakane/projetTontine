from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
 
class loginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", 
        widget = forms.TextInput(
        attrs={
            "class": "form-control"
        }
        ))
    password = forms.CharField(label="Mot de pass", widget = forms.PasswordInput(
        attrs={
            "class": "form-control"
        }
        ))
    


class SignUpForm(UserCreationForm):
    
    username = forms.CharField(label="Nom d'utilisateur", 
        widget = forms.TextInput(
        attrs={
            "class": "form-control"
        }
        ))
    
    
    email = forms.EmailField(label="E-mail", 
        widget = forms.TextInput(
        attrs={
            "class": "form-control"
        }
        ))
    
    password1 = forms.CharField(label="Mot de pass", widget = forms.PasswordInput(
        attrs={
            "class": "form-control"
        }
        ))
     
    password2 = forms.CharField(label="Confirmation de mot de pass", widget = forms.PasswordInput(
        attrs={
            "class": "form-control"
        }
        ))
    

    
 
    
class Meta:
    Model = User
    fields = ('username', 'email', 'password1', 'password2')


class paiment(forms.Form):
    montant = forms.DecimalField(label='Montant du paiement', max_digits=10, decimal_places=2)
    tour = forms.CharField(label='Numéro de carte', max_length=16)
    expiry_date = forms.CharField(label='Date d\'expiration (MM/YY)', max_length=5)
