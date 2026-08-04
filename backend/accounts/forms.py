from django.contrib.auth.forms import UserCreationForm
from .models import UserAccount

class UsercreationForm(UserCreationForm):
    class Meta:
        model=UserAccount
        fields=['username','password','email','Admission_number','phone','user_type']
