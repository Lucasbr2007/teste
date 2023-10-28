from django import forms
from . import models

class AlunoForm(forms.ModelForm):

    model = models.Aluno
    fields = '__all__'