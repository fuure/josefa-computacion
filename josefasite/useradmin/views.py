from django.shortcuts import render, redirect
from .models import MyModel
from .forms import MyModelForm

def index(request):
    items = MyModel.objects.all()
    return render(request, 'useradmin/index.html', {'items': items})

def create_item(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MyModelForm()
    return render(request, 'useradmin/create_item.html', {'form': form})
