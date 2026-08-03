from django.contrib.auth.forms import UserCreationForm
from .models import UserAccount

class UsercreationForm(UserCreationForm):
    class Meta:
        model=UserAccount
        fields={'username','password','email','admission_number','phone','usertype'}
