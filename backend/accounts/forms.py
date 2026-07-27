from django import forms
from .models import UserAccount

class UsercreationForm(forms.ModelForm):
    class Meta:
        model=UserAccount
        fields={'username','password','email','admission_number','phone','usertype'}
