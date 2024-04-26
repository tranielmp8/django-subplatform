
from django.forms import ModelForm
from account.models import CustomUser


# Creating a form based off the custom user
class UpdateUserForm(ModelForm):
  password = None
  
  class Meta:
    model = CustomUser
    fields = ['email', 'first_name', 'last_name',]
    exclude = ['password1', 'password2']