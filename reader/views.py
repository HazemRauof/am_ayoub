from django.shortcuts import render,redirect
from reader.models import UserForm

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()
    return render(request,'reader/signup.html',{'form':form})

# Create your views here.
