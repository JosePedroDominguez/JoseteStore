from django.shortcuts import redirect, render

from registroApp.forms import  CustomUserForm

from django.contrib import messages

from django.contrib.auth import authenticate, login

# Create your views here.

def registro(request):
    data={
        'form': CustomUserForm() 
    }
    if request.method == 'POST':
        formulario = CustomUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user= authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Cuenta Creada Exitosamente")
            return redirect(to="Home")
        data["form"] = formulario

    return (render(request, 'registration/registro.html',data))

