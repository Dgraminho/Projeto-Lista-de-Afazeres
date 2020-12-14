from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_itens = List.objects.all
            messages.success(request, ('Item adicionado!'))
            return render(request, 'home.html', {'all_itens': all_itens})

    else:
        all_itens = List.objects.all
        return render(request, 'home.html', {'all_itens': all_itens})

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ("Item Deletado!"))
    return redirect('home')

def check(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncheck(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ('Editado com sucesso!'))
            return redirect("home")

    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})