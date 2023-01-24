from django import forms
from .models import Items,Topics
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm


class WriteForm(forms.ModelForm):
    class Meta:
        #モデルを指定
        model = Items
        #フォームとして表示したいカラムを指定
        fields = ('text',)


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = ('title',)
        
class LoginForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       #htmlの表示を変更可能にします
       self.fields['username'].widget.attrs['class'] = 'form-control'
       self.fields['password'].widget.attrs['class'] = 'form-control'
            
class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能にします
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        
    class Meta:
        model = User
        fields = ('username','password1','password2',)