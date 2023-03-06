from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipos, Monitores, Perifericos, Asignacion
from .forms import AsignacionForm, EquiposForm, MonitoresForm, PerifericosForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.contrib import messages

# === INDEX ====

def home(request):
    return render(request, 'home.html')

# === LOGIN  ====

def login(request):
    return render(request, 'registration/login.html')


# === MENU DASHBOARD ====
def panel(request):
    asignacion = Asignacion.objects.all()

    listar_asignaciones = Asignacion.objects.all()
    listar_equipos = Equipos.objects.all()
    listar_monitores = Monitores.objects.all()
    listar_perisfericos = Perifericos.objects.all()


    total_listarasignaciones = listar_asignaciones.count()
    total_equipos = listar_equipos.count()
    total_monitores = listar_monitores.count()
    total_perisfericos = listar_perisfericos.count()

    context = {
        'listar_asignaciones': listar_asignaciones,
        'total_listarasignaciones': total_listarasignaciones,
        'total_equipos': total_equipos,
        'total_monitores': total_monitores,
        'total_perisfericos': total_perisfericos,
        'asignacion': asignacion,

    }
    return render(request, 'panel.html', context)


# === MENU ASIGNACION ====

def asignacion(request):
    data = {
        'form': AsignacionForm()
    }
    if request.method == 'POST':
        formulario = AsignacionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Se han ingresado los datos correctamente."
        else:
            data['form'] = formulario

    return render(request, 'Asignar/asignacion.html', data)



def modificarasignacion(request, id):
    asignacion = get_object_or_404(Asignacion, id=id)

    data = {
        'form':AsignacionForm(instance=asignacion)
    }
    if request.method == 'POST':
        formulario = PerifericosForm(data=request.POST, instance=asignacion)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="panel")
        data["form"] = formulario

    return render(request, 'Asignar/modificarasignacion.html', data)

def eliminarasignacion(request, id):
    eliminarasignacion = get_object_or_404(Asignacion, id=id)
    eliminarasignacion.delete()
    return redirect(to="panel")





def listarequipos(request):
    listar = Equipos.objects.all()
    busqueda_equipo = request.GET.get("busqueda_equipo")

    if busqueda_equipo:
        listar = Equipos.objects.filter(
            Q(codigo__icontains=busqueda_equipo) |
            Q(serieproducto__icontains=busqueda_equipo) |
            Q(tipo__icontains=busqueda_equipo) |
            Q(marca__icontains=busqueda_equipo)
        ).distinct()

    context = {
        'listar': listar,
        'busqueda_equipo': busqueda_equipo

    }

    return render(request, 'Equipos/listarequipos.html', context)


def modificarequipos(request, id):
    equipos = get_object_or_404(Equipos, id=id)

    context = {
        'form':EquiposForm(instance=equipos)
    }
    if request.method == 'POST':
        formulario = EquiposForm(data=request.POST, instance=equipos)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarequipos")
        context["form"] = formulario

    return render(request, 'Equipos/modificarequipos.html', context)


def eliminarequipos(request, id):
    eliminarequipo = get_object_or_404(Equipos, id=id)
    eliminarequipo.delete()
    return redirect(to="listarequipos")



# === MENU EQUIPOS ====

def equipos(request):
    data = {
        'form': EquiposForm()
    }
    if request.method == 'POST':
        formulario = EquiposForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Se han ingresado los datos correctamente."
        else:
            data['form'] = formulario

    return render(request, 'Equipos/equipos.html', data)


def listarequipos(request):
    listar = Equipos.objects.all()

    context = {
        'listar': listar,
    }
    return render(request, 'Equipos/listarequipos.html', context)


def modificarequipos(request, id):
    equipos = get_object_or_404(Equipos, id=id)

    data = {
        'form':EquiposForm(instance=equipos)
    }
    if request.method == 'POST':
        formulario = EquiposForm(data=request.POST, instance=equipos)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarequipos")
        data["form"] = formulario

    return render(request, 'Equipos/modificarequipos.html', data)


def eliminarequipos(request, id):
    eliminarequipo = get_object_or_404(Equipos, id=id)
    eliminarequipo.delete()
    return redirect(to="listarequipos")


# === MENU MONITORES ====

def monitores(request):
    data = {
        'form': MonitoresForm()
    }
    if request.method == 'POST':
        formulario = MonitoresForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Se han ingresado los datos correctamente."
        else:
            data["form"] = formulario

    return render(request, 'Monitores/monitores.html', data)


def listarmonitores(request):
    listar = Monitores.objects.all()

    data = {
        'listar': listar
    }
    return render(request, 'Monitores/listarmonitores.html', data)


def modificarmonitores(request, id):
    monitores = get_object_or_404(Monitores, id=id)

    data = {
        'form':MonitoresForm(instance=monitores)
    }
    if request.method == 'POST':
        formulario = MonitoresForm(data=request.POST, instance=monitores)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarmonitores")
        data["form"] = formulario

    return render(request, 'Monitores/modificarmonitores.html', data)


def eliminarmonitores(request, id):
    eliminarmonitor = get_object_or_404(Monitores, id=id)
    eliminarmonitor.delete()
    return redirect(to="listarmonitores")


# === MENU PERIFERICOS ====

def perifericos(request):
    data = {
        'form': PerifericosForm()
    }
    if request.method == 'POST':
        formulario = PerifericosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Se han ingresado los datos correctamente."
        else:
            data["form"] = formulario

    return render(request, 'Perifericos/perifericos.html', data)


def listarperifericos(request):
    listar = Perifericos.objects.all()

    data = {
        'listar': listar
    }
    return render(request, 'Perifericos/listarperifericos.html', data)

def modificarperisferico(request, id):
    perisfericos = get_object_or_404(Perifericos, id=id)

    data = {
        'form':PerifericosForm(instance=perisfericos)
    }
    if request.method == 'POST':
        formulario = PerifericosForm(data=request.POST, instance=perisfericos)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarperifericos")
        data["form"] = formulario

    return render(request, 'Perifericos/modificarperisfericos.html', data)

def eliminarperisfericos(request, id):
    eliminarperisferico = get_object_or_404(Perifericos, id=id)
    eliminarperisferico.delete()
    return redirect(to="listarperifericos")


# === MENU REGISTRO CUENTAS ====

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request)
            messages.success(request, "Te has registrado en forma exitosa")
            return redirect(to="login")
        data["form"] = formulario
    return render(request, './registration/registro.html', data)




