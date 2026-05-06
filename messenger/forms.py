from django import forms
from .models import Message
from django.contrib.auth.models import User

class MessageForm(forms.ModelForm):
    receiver = forms.ModelChoiceField(queryset=User.objects.all(), label='Para')
    
    class Meta:
        model = Message
        fields = ['receiver', 'content']
        labels = {
            'content': 'Mensaje',
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }
        