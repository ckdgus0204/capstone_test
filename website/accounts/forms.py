from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CreateUserForm(UserCreationForm):
    email=forms.EmailField(required=True)
    name=forms.CharField(required=True)
    class Meta:
        model = User
        fields=('username','password1','password2','name','email')

    def save(self, commit=True):
        user=super(CreateUserForm,self).save(coomit=False)
        user.name=self.cleaned_data["name"]
        user.email=self.cleaned_data["email"]
        if commit:
            user.save()
        return user