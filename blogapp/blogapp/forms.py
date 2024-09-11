from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment

class RegisterForm(UserCreationForm): 
    email = forms.EmailField()
    password2 = forms.CharField(label="Confirm Password",widget=forms.TextInput(attrs={'type': 'text'}))
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm): 
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']


class CommentForm(forms.ModelForm): 
    class Meta: 
        model = Comment
        fields = ['content']

class PostForm(forms.ModelForm): 
    class Meta: 
        model = Post
        fields = ['title', 'description']