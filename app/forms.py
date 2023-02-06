from django import forms
from django.core import validators

def validators_for_h(value):
    if value[0]=='h':
        raise forms.ValidationError('name is starting with h')

def check_for_len(value):
    if value[0]<5:
        raise forms.ValidationError('len is too low')

class NameForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[validators_for_h])
    age=forms.IntegerField()
    mail=forms.EmailField(max_length=100)
    remail=forms.EmailField(max_length=100)
    mobileN=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)#true


    def clean(self):
        e=self.cleaned_data['mail']
        re=self.cleaned_data['remail']
        if e!=re:
            raise forms.ValidationError('not matched')

    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot is catched')
    
