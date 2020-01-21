from django import forms
from .models import Comment
class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Get author from value of author key
        self.author = kwargs.pop('author', None)
        self.post   = kwargs.pop('post', None)
        # Override for parent class
        super().__init__(*args, **kwargs)
    def save(self, commit=True):
        comment        = super().save(commit=False)
        comment.author = self.author
        comment.post   = self.post
        comment.save()
    class Meta:
        model  = Comment
        fields = ['content'] 