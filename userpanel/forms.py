from django import forms
from.models import Blog
from.models import ProfileUser
from.models import Comment

class blogform(forms.ModelForm):
    class Meta:
        model =Blog
        fields ='__all__'

class userform(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields ="__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
