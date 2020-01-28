from django import forms
from django.contrib.auth import forms as auth_forms
from blog.models import Post, Comment, Subscriber


class CustomAuthForm(auth_forms.AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "validate",
                                                       "placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"type": "password",
                                                            "placeholder": "Password"}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("author", "title", "text", "image")

        widgets = {
            "title": forms.TextInput(),
            "text": forms.Textarea(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("author", "text")

        widgets = {
            "author": forms.TextInput(),
            "text": forms.Textarea(),
        }

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ("email",)

        widgets = {
            "email": forms.EmailInput(attrs={"placeholder": "Your email address.."}),
        }
