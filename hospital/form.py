from django import forms
from .models import User,Users

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class RegisterForm(forms.ModelForm):
    # confirm = forms.CharField(max_length=10, min_length=1)
    # def  clean(self):
    #     cleaned_data = super(RegisterForm, self).clean()
    #     password = cleaned_data.get("password")

    class Meta:
        model = Users
        fields = ['username','password','realname','email','status','role']












