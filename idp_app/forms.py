from django import forms
from idp_app.models import Situation
from django.core.files.uploadedfile import InMemoryUploadedFile
from idp_app.humanize import naturalsize

from django.core.exceptions import ValidationError
from django.core import validators



class CommentForm(forms.Form):
    comment = forms.CharField(required=True, max_length=500, min_length=3, strip=True)
