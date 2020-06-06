from django.db import models
from django import forms
from blog.models import *


class post_form(forms.ModelForm):
    class Meta:
        model=blog_model
        fields='__all__'
