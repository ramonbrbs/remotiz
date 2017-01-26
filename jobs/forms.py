from django import forms
from .models import Job
from captcha.fields import ReCaptchaField

class AddJobForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Job
        fields = ('title', 'description', 'submitInfo')