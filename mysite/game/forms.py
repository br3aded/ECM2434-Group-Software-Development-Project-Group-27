from django import forms
from . import models

class createSubmission(forms.ModelForm):
    class Meta:
        model = models.Submission
        fields = ['submission']
