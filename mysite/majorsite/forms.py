from django import forms

from majorsite.models import User, UserFiles, Post

class AvatarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('avatar',)

class AudiosForm(forms.ModelForm):
    class Meta:
        model = UserFiles
        fields = ('audios',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'content',)

