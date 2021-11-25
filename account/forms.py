from django.forms import ModelForm, PasswordInput, ValidationError, CharField, EmailField
from django.forms.widgets import TextInput, EmailInput
from django.contrib.auth.hashers import check_password
from .models import User

class UserLoginForm(ModelForm):
    email = EmailField(max_length=150, widget=EmailInput(attrs={'placeholder': 'Enter your email'}), required=False)
    password = CharField(max_length=50, widget=PasswordInput(attrs={'placeholder': 'Enter your password'}), required=False)
    class Meta:
        model = User
        fields = ['email', 'password']

    def clean(self):
        cleaned_data = super(UserLoginForm,self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if not email or not password:
            raise ValidationError('All required fields must be filled')
        if not User.objects.filter(email=email).exists():
            raise ValidationError('Email is not exists. Please register')
        user_password = User.objects.get(email=email).password
        print(password, user_password)
        if not check_password(password, user_password):
            raise ValidationError('Incorrect password')
        return cleaned_data

       

class UserRegistrationForm(ModelForm):
    username = CharField(max_length=50, widget=TextInput(attrs={'placeholder': 'Enter yourname'}), required=False)
    email = EmailField(max_length=150, widget=EmailInput(attrs={'placeholder': 'Enter your email'}), required=False)
    password = CharField(max_length=50, widget=PasswordInput(attrs={'placeholder': 'Enter your password'}), required=False)
    confirm_password = CharField(max_length=50, widget=PasswordInput(attrs={'placeholder': 'Confirm your password'}), required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        

    def clean(self):
        cleaned_data = super(UserRegistrationForm,self).clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        print(username, email, password, confirm_password)
        if not username or not email or not password or not confirm_password:
            raise ValidationError('All required fields must be filled')
        if password != confirm_password:
            raise ValidationError('Password and confirm_password does not match')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email is exists')
        if len(password) < 8:
            raise ValidationError('Password must have at least 8 chars')
        return cleaned_data

    
        
        
        

    





