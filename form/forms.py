from sys import path

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms

from form import views


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    app_name = 'main'  # here for namespacing of urls.

    urlpatterns = [
        path("", views.homepage, name="homepage"),
        path("register/", views.register, name="register"),
    ]