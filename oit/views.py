
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import OIT
from .forms import OITForm



@login_required
def listar_oits(request):
    oits = OIT.objects.all()  # O modifica según tus necesidades
    return render(request, 'listar_oits.html', {'oits': oits})

@login_required
def crear_oit(request):
    if request.method == 'GET':
        return render(request, 'crear_oit.html', {
            'form': OITForm()
        })
    else:
        try:
            form = OITForm(request.POST)
            new_oit = form.save(commit=False)
            # Agrega cualquier dato adicional antes de guardar, si es necesario
            new_oit.save()
            return redirect('listar_oits')
        except ValueError:
            return render(request, 'crear_oit.html', {
                'form': OITForm(),
                'error': 'Por favor, proporciona datos válidos.'
            })

@login_required
def detalle_oit(request, oit_id):
    oit = get_object_or_404(OIT, pk=oit_id)
    if request.method == 'GET':
        form = OITForm(instance=oit)
        return render(request, 'detalle_oit.html', {'oit': oit, 'form': form})
    else:
        try:
            form = OITForm(request.POST, instance=oit)
            form.save()
            return redirect('listar_oits')
        except ValueError:
            return render(request, 'detalle_oit.html', {
                'oit': oit,
                'form': form,
                'error': 'Error actualizando la OIT.'
            })

@login_required
def eliminar_oit(request, oit_id):
    oit = get_object_or_404(OIT, pk=oit_id)
    if request.method == 'POST':
        oit.delete()
        return redirect('listar_oits')
"""



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import OIT
from .forms import OITForm
from django.http import HttpResponseNotAllowed




@login_required
def listar_oits(request):
    oits_activas = OIT.objects.filter(completado=False)  # Asumiendo que 'completado' es un campo booleano en tu modelo OIT
    return render(request, 'listar_oits.html', {'oits': oits_activas})

@login_required
def oits_completadas(request):
    oits_completadas = OIT.objects.filter(completado=True)
    return render(request, 'oits_completadas.html', {'oits': oits_completadas})

@login_required
def crear_oit(request):
    if request.method == 'GET':
        return render(request, 'crear_oit.html', {'form': OITForm()})
    else:
        try:
            form = OITForm(request.POST)
            nueva_oit = form.save(commit=False)
            nueva_oit.usuario = request.user
            nueva_oit.save()
            return redirect('listar_oits')
        except ValueError:
            return render(request, 'crear_oit.html', {'form': OITForm(), 'error': 'Datos no válidos'})

@login_required
def detalle_oit(request, oit_id):
    oit = get_object_or_404(OIT, pk=oit_id)
    if request.method == 'GET':
        form = OITForm(instance=oit)
        return render(request, 'detalle_oit.html', {'oit': oit, 'form': form})
    else:
        try:
            form = OITForm(request.POST, instance=oit)
            form.save()
            return redirect('listar_oits')
        except ValueError:
            return render(request, 'detalle_oit.html', {'oit': oit, 'form': form, 'error': 'Error al actualizar la OIT'})

@login_required
def completar_oit(request, oit_id):
    oit = get_object_or_404(OIT, pk=oit_id)
    if request.method == 'POST':
        oit.fecha_completado = timezone.now()
        oit.save()
        return redirect('listar_oits')

@login_required
def eliminar_oit(request, oit_id):
    oit = get_object_or_404(OIT, pk=oit_id)
    
    if request.method == 'POST':
        oit.delete()
        return redirect('listar_oits')
    else:
        # Si no quieres permitir el método GET, puedes responder con un error.
        return HttpResponseNotAllowed(['POST'], 'Método no permitido')

@login_required
def editar_oit(request, oit_id):
    oit = get_object_or_404(OIT, pk=oit_id)
    if request.method == 'POST':
        form = OITForm(request.POST, instance=oit)
        if form.is_valid():
            form.save()
            return redirect('detalle_oit', oit_id=oit.id)
    else:
        form = OITForm(instance=oit)
    return render(request, 'editar_oit.html', {'form': form, 'oit': oit})



    