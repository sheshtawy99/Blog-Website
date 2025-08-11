from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "User_name": "Your Name",
            "User_Email": "Yout Email",
            "text": "Your Comment"
        }
