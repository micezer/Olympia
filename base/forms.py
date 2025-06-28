from django.forms import ModelForm
from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Service  # o desde la app correspondiente



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [ 'username', 'email', ]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'birth_date', 'services']  # SOLO campos de UserProfile
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'services': forms.CheckboxSelectMultiple(),
        }



class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("Username already exists")
        return username  

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Email already in use")
        return email

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=False)
    birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields  # Typically ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=commit)
        user_profile = UserProfile.objects.get(user=user)
        user_profile.phone = self.cleaned_data['phone']
        user_profile.birth_date = self.cleaned_data['birth_date']
        if commit:
            user_profile.save()
        return user