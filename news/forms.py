from django import forms

from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["user", "title", "content", "image", "draft", "publish"]