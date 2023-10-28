from django.shortcuts import render

from . import models, forms

def home(request):
    aluno = models.Aluno.objects.all()
    return render(request, 'home.html' , {'estudante': aluno}) 

def page1(request):
    form = forms.AlunoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        return render(request, 'page1.html')

def delete(request, id):
    delete = models.Aluno.objects.get(id=id)
    delete.delete()
    return redirect('home')
