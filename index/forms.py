from django import forms
from index.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model =  User
        fileds = "__all__"
        widgets = {
            "upwd" : forms.PasswordInput
        }