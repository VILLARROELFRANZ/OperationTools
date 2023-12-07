from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            # En lugar de un mensaje de error estático, puedes mostrar errores específicos del formulario.
            return render(request, 'signin.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

@login_required
def signout(request):
    logout(request)
    # Considera redirigir a la página de inicio de sesión después de cerrar sesión.
    return redirect('signin')



