from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'image']

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data['title']
        qs = Post.objects.filter(title=title)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("This title already exists.")
        return title

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) < 50:
            raise forms.ValidationError('Content must be at least 50 characters')
        return content
