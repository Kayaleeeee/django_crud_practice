from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'contents', 'price', 'rating', 'img',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        labels = {
            'content': (''),
            # 위에 콘텐트는 장고에서 이미 정해준 이름
        }

        widgets = {
            'content': forms.Textarea(attrs={'placeholder': '댓글을 입력해주세요.'})
        }
