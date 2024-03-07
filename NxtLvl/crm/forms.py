from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import ClientRecord


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.forms.widgets import DateTimeInput

# Create/Register a User

class CreateUserForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username', 'password1', 'password2']
        
        

# Login a User

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
        
# Add a Record 
class AddRecordForm(forms.ModelForm):
    
    class Meta:
        
        model = ClientRecord
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'country', 'company_name', 'work_info', 'start_date', 'current_status', 'progress_percentage', 'delivery_date', 'deal_amount']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'start_date', 'delivery_date',
            Submit('submit', 'save')
        )
        self.fields['start_date'].widget = DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        self.fields['delivery_date'].widget = DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        
        

# Update a Record 
class UpdateRecordForm(forms.ModelForm):
    
    class Meta:
        
        model = ClientRecord
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'country', 'company_name', 'work_info', 'start_date', 'current_status', 'progress_percentage', 'delivery_date', 'deal_amount']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'start_date', 'delivery_date',
            Submit('submit', 'save')
        )
        self.fields['start_date'].widget = DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        self.fields['delivery_date'].widget = DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')