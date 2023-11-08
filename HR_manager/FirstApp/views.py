from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def register(request):

    if request.method == 'GET':

        return render(request, "FirstApp/register.html", {'form': UserCreationForm})

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('Principal')  

            except:
        
                return render(request, "FirstApp/register.html", {'form': UserCreationForm, "error":'El usuario existe'}) 
            
    return render(request, "FirstApp/register.html", {'form': UserCreationForm, "error":'Los password no coinciden'})


def home(request):
    #inicio
    return render(request, "FirstApp/home.html")


def close(request):

    logout(request)

    return redirect('logueo')  


def access(request):

    if request.method == 'GET':
        return render(request, 'FirstApp/access.html', {'form': AuthenticationForm})

    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'FirstApp/access.html', {'form': AuthenticationForm, 'error':'los datos son incorrectos'})

        else:
            login(request, user)
            return redirect('Principal')

def createHoja1(request):
    if request.method == 'GET':
        return render(request, 'FirstApp/createH1.html', {'form': CreateHoja1})
    else:
        try:
            form = CreateHoja1(request.POST)
            form.save()
            return redirect('Principal')
        except ValueError:
            return render(request, 'FirstApp/createH1.html', {'form': CreateHoja1, 'error':'Dato no valido'})

def readHoja1(request):
    leeH1 = Hoja1.objects.all()   #leeH1 = Hoja1.objects.filter(dni = request.dni)
    contexto = {'leeH1':leeH1}
    return render(request, "FirstApp/readH1.html", contexto )    

def detailHoja1(request, id):
    if request.method == 'GET':
        detalle = get_object_or_404(Hoja1, pk=id)
        form = CreateHoja1(instance=detalle)
        return render(request, "FirstApp/detailH1.html", {'detalle': detalle, 'form': form})
    else:
        try:
            detalle = get_object_or_404(Hoja1, pk=id)
            form = CreateHoja1(request.POST, instance=detalle)
            form.save()
            return redirect('Principal')
        except ValueError:
            return render(request, "FirstApp/detailH1.html", {'detalle': detalle, 'form': form, 'error': "error de actualizacion" })
        
def eraseH1(request):
    if request.method == "POST":
        dni = request.POST.get('dni')
        try:
            legajo = Hoja1.objects.get(dni=dni)
            legajo.delete()
        except Hoja1.DoesNotExist:
            # ver que hacer si pone un valor que no existe
            pass

    legajo = Hoja1.objects.all()
    contexto = {"legajo": legajo}
    return render(request, "FirstApp/eraseH1.html", contexto)

def libro_de_reclamos(request):
    mensajes = Mensaje.objects.all().order_by('-fecha_creacion')
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MensajeForm()

    return render(request, 'FirstApp/libro_de_reclamos.html', {'mensajes': mensajes, 'form': form})

def biografia(request):
    #de mi
    return render(request, "FirstApp/biografia.html")

def ver_tablas(request):
    hoja2_registros = Hoja2.objects.all()
    capacitacion_registros = Capacitacion.objects.all()

    return render(request, 'FirstApp/ver_tablas.html', {
        'hoja2_registros': hoja2_registros,
        'capacitacion_registros': capacitacion_registros,
    })

def editar_registro_hoja2(request, registro_id):
    hoja2_registro = Hoja2.objects.get(id=registro_id)
    if request.method == 'POST':
        form = Hoja2Form(request.POST, instance=hoja2_registro)
        if form.is_valid():
            form.save()
            return redirect('ver_tablas')
    else:
        form = Hoja2Form(instance=hoja2_registro)
    return render(request, 'FirstApp/editar_registro.html', {
        'form': form,
        'model_name': 'Hoja2',
    })

def editar_registro_capacitacion(request, registro_id):
    capacitacion_registro = Capacitacion.objects.get(id=registro_id)
    if request.method == 'POST':
        form = CapacitacionForm(request.POST, instance=capacitacion_registro)
        if form.is_valid():
            form.save()
            return redirect('ver_tablas')
    else:
        form = CapacitacionForm(instance=capacitacion_registro)
    return render(request, 'FirstApp/editar_registro.html', {
        'form': form,
        'model_name': 'Capacitacion',
    })

def nuevo_registro_hoja2(request):
    if request.method == 'POST':
        form = Hoja2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_tablas')
    else:
        form = Hoja2Form()
    return render(request, 'FirstApp/nuevo_registro.html', {
        'form': form,
        'model_name': 'Hoja2',
    })

def nuevo_registro_capacitacion(request):
    if request.method == 'POST':
        form = CapacitacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_tablas')
    else:
        form = CapacitacionForm()
    return render(request, 'FirstApp/nuevo_registro.html', {
        'form': form,
        'model_name': 'Capacitacion',
    })