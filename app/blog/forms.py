from blog.models import Post
from django import forms
from wmd.widgets import WMDWidget


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=WMDWidget())

    class Meta:
        model = Post
        exclude = ()
