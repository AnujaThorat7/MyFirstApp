#from django.http import HttpResponse
#from django.shortcuts import render
#from . models import Register


#def index(request):
#    register = Register.objects.all()
#    return render(request,'index.html', {'register': register})

from django.shortcuts import render, redirect
from register.forms import RegisterForm
from register.models import Register
# Create your views here.


def user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = RegisterForm()
    return render(request,'index.html', {'form': form})


def show(request):
    register = Register.objects.all()
    return render(request, "show.html", {'register': register})


def edit(request, id):
    register = Register.objects.get(id=id)
    return render(request,'edit.html', {'register': register})


def update(request, id):
    register = Register.objects.get(id=id)
    form = RegisterForm(request.POST, instance=register)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'register': register})


def destroy(request, id):
    register = Register.objects.get(id=id)
    register.delete()
    return redirect("/show")

