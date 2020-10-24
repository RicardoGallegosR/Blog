from django import forms
from .models import Post, Comment
from ckeditor.widgets import CKEditorWidget

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    class Meta:
        model = Comment
        fields = ('content', )

class PostForm(forms.ModelForm):
    """form =  forms.CharField(widget = CKEditorWidget())"""
    class Meta:
        model = Post
        fields  = ('title', 'overview', 'content', 'thumbnail', 
        'categories', 'featured', 'previous_post', 'next_post')

