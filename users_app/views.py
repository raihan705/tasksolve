from django.shortcuts import render,redirect
from users_app.forms import customRegistration
from django.contrib import messages

# Create your views here.



def register(request):
    if request.method == 'POST':
        register_form = customRegistration(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')
        
    

    else:
        register_form = customRegistration()

    return render(request, 'register.html', {'register_form': register_form})

    