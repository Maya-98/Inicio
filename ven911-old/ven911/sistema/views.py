from django.shortcuts import render, redirect
from sistema.forms import ReglamentsForm, NormativasForm, EntradapForm, SalidapForm, GestionForm, UserCreateForm, DepartamentosForm, SedesForm, VehiculosForm, PresupuestoForm, UserUpdateForm, UserUpdatePForm, DepartamentosEForm, SedesEForm, ReglamentsUForm, ReglamentsUFForm, NormativasUForm, NormativasUFForm, EntradapEForm, SalidapEForm, GestionEForm, VehiculosEForm, PresupuestoEForm, GestionHForm, GestionEHForm, IncidenciasForm, IncidenciasEForm
from sistema.models import Reglamentos, Normativas, Entradap, Salidap, Gestion, UserC, Departamentos, Sedes, Vehiculos, Presupuesto, UserC, Personal, Incidencias
from django.contrib.auth import authenticate, login as auth_login, logout 
from .decorators import no_autenticado, allowed_users

from django.contrib.auth.decorators import login_required

# VISTAS DE INDEX
@login_required(login_url='login')
def index(request):
    context = {}
    return render(request, "modulos.html", context)

def modulos(request):
    return render(request, "modulos.html")

# VISTAS DE LOGIN 
@no_autenticado
def loginf(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            if user.tipo == 'admin':
                return redirect('/')
            elif user.tipo == 'estandar':
                return redirect('/organizacion')
            elif user.tipo == 'coordinador':
                return redirect('/seguridad')
        else:
            return render(request, "login_error.html")
    
    context = {}
    return render(request, "login.html", context)

# VISTAS DE LOGOUT 
def logoutUser(request):
    logout(request)
    return redirect('/')

# VISTAS DE 403
def loginf403(request):
    return render(request, "403.html")

# VISTAS DE ADMIN
@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def usuarios(request):
    if request.method == 'POST':
        forml = UserCreateForm(request.POST)
        if forml.is_valid():
            forml.save()
            return redirect("/admin/#success")
        else:
            context = {'forml': forml}
            return redirect("/admin/#failed")
    usersl = UserC.objects.all()
    departamentosp = Departamentos.objects.all()
    sedesp = Sedes.objects.all()
    context = {'forml': UserCreateForm(), 'usersl': usersl, 'departamentosp': departamentosp, 'sedesp': sedesp}
    return render(request, 'admin/usuarios.html', context)

# VISTAS DE CREACIÓN Y LISTA DE USUARIOS - ADMIN
@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def usuarios(request):
    if request.method == 'POST':
        forml = UserCreateForm(request.POST)
        if forml.is_valid():
            forml.save()
            return redirect("/admin#success")
        else:
            context = {'forml': forml}
            return redirect("/admin#failed")
    usersl = UserC.objects.all()
    departamentosp = Departamentos.objects.all()
    sedesp = Sedes.objects.all()
    context = {'formuu': UserUpdateForm(), 'formpp': UserUpdatePForm(), 'forml': UserCreateForm(), 'usersl': usersl, 'departamentosp': departamentosp, 'sedesp': sedesp}
    return render(request, 'admin/usuarios.html', context)

# VISTAS DE ACTUALIZACIÓN DE USUARIOS - ADMIN
def update_usuarios(request, id):
    queryset = UserC.objects.get(id=id)
    form = UserUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/admin#updatesuccess')

# VISTAS DE ACTUALIZACIÓN DE PASSWORD DE USUARIOS - ADMIN
def updatep_usuarios(request, id):
    queryset = UserC.objects.get(id=id)
    form = UserUpdatePForm(instance=queryset)
    if request.method == 'POST':
        form = UserUpdatePForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/admin#updatesuccess')

# VISTAS DE ELIMINACIÓN DE USUARIOS - ADMIN
def del_usuarios(request, id):
    if request.method == 'POST':
        users = UserC.objects.get(id=id)
        users.delete()
        return redirect('/admin#deletesuccess')

# VISTAS DE CREACIÓN Y LISTA DE DEPARTAMENTOS - ADMIN
@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def departamentos(request):
    if request.method == 'POST':
        form6 = DepartamentosForm(request.POST)
        if form6.is_valid():
            form6.save()
            return redirect("/admin/departamentos#success")
        else:
            context = {'form6': form6}
            return render(request, 'admin/departamentos.html', context)
    departamentosp = Departamentos.objects.all()
    context = {'formdp': DepartamentosEForm(),'form6': DepartamentosForm(), 'departamentosp': departamentosp}
    return render(request, 'admin/departamentos.html', context)

# VISTAS DE ACTUALIZACIÓN DE DEPARTAMENTOS - ADMIN
def update_departamentos(request, id):
    queryset = Departamentos.objects.get(id=id)
    form = DepartamentosEForm(instance=queryset)
    if request.method == 'POST':
        form = DepartamentosEForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/admin/departamentos#updatesuccess')

# VISTAS DE ELIMINACIÓN DE DEPARTAMENTOS - ADMIN
def del_departamentos(request, id):
    if request.method == 'POST':
        form = Departamentos.objects.get(id=id)
        form.delete()
        return redirect('/admin/departamentos#deletesuccess')

# VISTAS DE CREACIÓN Y LISTA DE SEDES - ADMIN
@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def sedes(request):
    if request.method == 'POST':
        form7 = SedesForm(request.POST)
        if form7.is_valid():
            form7.save()
            return redirect("/admin/sedes#success")
        else:
            context = {'form7': form7}
            return render(request, 'admin/sedes.html', context)
    sedesp = Sedes.objects.all()
    context = {'form7': SedesForm(), 'formsp': SedesEForm(), 'sedesp': sedesp}
    return render(request, 'admin/sedes.html', context)

# VISTAS DE ACTUALIZACIÓN DE SEDES - ADMIN
def update_sedes(request, id):
    queryset = Sedes.objects.get(id=id)
    form = SedesEForm(instance=queryset)
    if request.method == 'POST':
        form = SedesEForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/admin/sedes#updatesuccess')

# VISTAS DE ELIMINACIÓN DE SEDES - ADMIN
def del_sedes(request, id):
    if request.method == 'POST':
        form = Sedes.objects.get(id=id)
        form.delete()
        return redirect('/admin/sedes#deletesuccess')

# VISTAS DE ORGANIZACIÓN
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'organizacion'])
def organizacion(request):
    reglamentoss = Reglamentos.objects.all()
    normativass = Normativas.objects.all()
    objetos = zip(reglamentoss, normativass)
    context = {'reglamentoss': reglamentoss, 'normativass': normativass, 'objetos': objetos}
    return render(request, "organizacion/organizacion.html", context)

# VISTAS DE REGLAMENTOS
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'organizacion'])
def reglamentos(request):
    if request.method == 'POST':
        form = ReglamentsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            context = {'form': form}
            return render(request, 'organizacion/reglamentos.html', context)
    reglamentoss = Reglamentos.objects.all()
    context = {'form': ReglamentsForm(), 'former': ReglamentsUForm(), 'formerf': ReglamentsUFForm(), 'reglamentoss': reglamentoss}
    return render(request, 'organizacion/reglamentos.html', context)

# VISTAS DE ACTUALIZACIÓN DE REGLAMENTOS
def update_reglamentos(request, id):
    queryset = Reglamentos.objects.get(id=id)
    form = ReglamentsUForm(instance=queryset)
    if request.method == 'POST':
        form = ReglamentsUForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/organizacion/reglamentos#updatesuccess')

# VISTAS DE ACTUALIZACIÓN DE ARCHIVOS DE REGLAMENTOS 
def update_reglamentosf(request, id):
    queryset = Reglamentos.objects.get(id=id)
    form = ReglamentsUFForm(instance=queryset)
    if request.method == 'POST':
        form = ReglamentsUFForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/organizacion/reglamentos#updatesuccess')

# VISTAS DE ELIMINACIÓN DE REGLAMENTOS
def del_reglamentos(request, id):
    if request.method == 'POST':
        form = Reglamentos.objects.get(id=id)
        form.delete()
        return redirect('/organizacion/reglamentos#deletesuccess')

# VISTAS DE NORMATIVAS
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'organizacion'])
def normativas(request):
    if request.method == 'POST':
        form5 = NormativasForm(request.POST, request.FILES)
        if form5.is_valid():
            form5.save()
        else:
            context = {'form5': form5}
            return render(request, 'organizacion/normativas.html', context)
    normativass = Normativas.objects.all()
    context = {'form5': NormativasForm(), 'formen': NormativasUForm(), 'formenf': NormativasUFForm(), 'normativass': normativass}
    return render(request, 'organizacion/normativas.html', context)

# VISTAS DE ACTUALIZACIÓN DE NORMATIVAS
def update_normativas(request, id):
    queryset = Normativas.objects.get(id=id)
    form = NormativasUForm(instance=queryset)
    if request.method == 'POST':
        form = ReglamentsUForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/organizacion/normativas#updatesuccess')

# VISTAS DE ACTUALIZACIÓN DE ARCHIVOS DE NORMATIVAS 
def update_normativasf(request, id):
    queryset = Normativas.objects.get(id=id)
    form = NormativasUFForm(instance=queryset)
    if request.method == 'POST':
        form = NormativasUFForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/organizacion/normativas#updatesuccess')

# VISTAS DE ELIMINACIÓN DE NORMATIVAS
def del_normativas(request, id):
    if request.method == 'POST':
        form = Normativas.objects.get(id=id)
        form.delete()
        return redirect('/organizacion/normativas#deletesuccess')

# VISTAS DE SEGURIDAD
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'seguridad'])
def seguridad(request):
    entradap = Entradap.objects.all()
    salidap = Salidap.objects.all()
    gestion = Gestion.objects.all()
    objetos = zip(entradap, salidap)
    context = {'gestion': gestion, 'entradap': entradap, 'salidap': salidap,'objetos': objetos}
    return render(request, "seguridad/seguridad.html", context)

# VISTAS DE ENTRADA DE PERSONAL
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'seguridad'])
def entradap(request):
    if request.method == 'POST':
        form2 = EntradapForm(request.POST)
        if form2.is_valid():
            form2.save()
        else:
            context = {'form2': form2}
            return render(request, 'seguridad/entradap.html', context)
    entradapp = Entradap.objects.all()
    context = {'form2': EntradapForm(), 'formeep': EntradapEForm(), 'entradapp': entradapp}
    return render(request, 'seguridad/entradap.html', context)

# VISTAS DE ACTUALIZACIÓN DE ENTRADA DE PERSONAL
def update_entradap(request, id):
    queryset = Entradap.objects.get(id=id)
    form = EntradapEForm(instance=queryset)
    if request.method == 'POST':
        form = EntradapEForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/seguridad/entradap#updatesuccess')

# VISTAS DE ELIMINACIÓN DE ENTRADA DE PERSONAL
def del_entradap(request, id):
    if request.method == 'POST':
        form = Entradap.objects.get(id=id)
        form.delete()
        return redirect('/seguridad/entradap#deletesuccess')

# VISTAS DE SALIDA DE PERSONAL
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'seguridad'])
def salidap(request):
    if request.method == 'POST':
        form3 = SalidapForm(request.POST)
        if form3.is_valid():
            form3.save()
        else:
            context = {'form3': form3}
            return render(request, 'seguridad/salidap.html', context)
    salidapp = Salidap.objects.all()
    context = {'form2': SalidapForm(), 'formesp': SalidapEForm(), 'salidapp': salidapp}
    return render(request, 'seguridad/salidap.html', context)

# VISTAS DE ACTUALIZACIÓN DE SALIDA DE PERSONAL
def update_salidap(request, id):
    queryset = Salidap.objects.get(id=id)
    form = SalidapEForm(instance=queryset)
    if request.method == 'POST':
        form = SalidapEForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/seguridad/salidap#updatesuccess')

# VISTAS DE ELIMINACIÓN DE SALIDA DE PERSONAL
def del_salidap(request, id):
    if request.method == 'POST':
        form = Salidap.objects.get(id=id)
        form.delete()
        return redirect('/seguridad/salidap#deletesuccess')

# VISTAS DE GESTIÓN DE INCIDENTES
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'seguridad'])
def gestions(request):
    if request.method == 'POST':
        form2 = GestionForm(request.POST)
        if form2.is_valid():
            form2.save()
        else:
            context = {'form2': form2}
            return render(request, 'seguridad/gestion.html', context)
    gestionp = Gestion.objects.all()
    context = {'form2': GestionForm(), 'formesp': GestionEForm(), 'gestionp': gestionp}
    return render(request, 'seguridad/gestion.html', context)

# VISTAS DE ACTUALIZACIÓN DE GESTIÓN DE INCIDENTES
def update_gestion(request, id):
    queryset = Gestion.objects.get(id=id)
    form = GestionEForm(instance=queryset)
    if request.method == 'POST':
        form = GestionEForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/seguridad/gestion#updatesuccess')

# VISTAS DE ELIMINACIÓN DE GESTIÓN DE INCIDENTES
def del_gestion(request, id):
    if request.method == 'POST':
        form = Gestion.objects.get(id=id)
        form.delete()
        return redirect('/seguridad/gestion#deletesuccess')

# VISTAS DE VEHÍCULOS
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'seguridad'])
def vehiculos(request):
    if request.method == 'POST':
        form8 = VehiculosForm(request.POST)
        if form8.is_valid():
            form8.save()
        else:
            context = {'form8': form8}
            return render(request, 'seguridad/vehiculos.html', context)
    vehiculoss = Vehiculos.objects.all()
    context = {'form8': VehiculosForm(), 'formesp': VehiculosEForm(), 'vehiculoss': vehiculoss}
    return render(request, 'seguridad/vehiculos.html', context)

# VISTAS DE ACTUALIZACIÓN DE GESTIÓN DE INCIDENTES
def update_vehiculos(request, id):
    queryset = Vehiculos.objects.get(id=id)
    form = VehiculosEForm(instance=queryset)
    if request.method == 'POST':
        form = VehiculosEForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/seguridad/vehiculos#updatesuccess')

# VISTAS DE ELIMINACIÓN DE GESTIÓN DE INCIDENTES
def del_vehiculos(request, id):
    if request.method == 'POST':
        form = Vehiculos.objects.get(id=id)
        form.delete()
        return redirect('/seguridad/vehiculos#deletesuccess')

# VISTAS DE PRESUPUESTO
@login_required(login_url='login')
def presupuesto(request):
    if request.method == 'POST':
        form9 = PresupuestoForm(request.POST)
        if form9.is_valid():
            form9.save()
        else:
            context = {'form9': form9}
            return render(request, 'presupuesto/presupuesto.html', context)
    presupuestoss = Presupuesto.objects.all()
    context = {'form9': PresupuestoForm(), 'formesp': PresupuestoEForm(), 'presupuestoss': presupuestoss}
    return render(request, 'presupuesto/presupuesto.html', context)

# VISTAS DE ACTUALIZACIÓN DE PRESUPUESTO
def update_presupuesto(request, id):
    queryset = Presupuesto.objects.get(id=id)
    form = PresupuestoEForm(instance=queryset)
    if request.method == 'POST':
        form = PresupuestoEForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/presupuesto#updatesuccess')

# VISTAS DE ELIMINACIÓN DE PRESUPUESTO
def del_presupuesto(request, id):
    if request.method == 'POST':
        form = Presupuesto.objects.get(id=id)
        form.delete()
        return redirect('/presupuesto#deletesuccess')

# VISTAS DE ASIGNACIÓN
@login_required(login_url='login')
def asignacion(request):
    if request.method == 'POST':
        form9 = PresupuestoForm(request.POST)
        if form9.is_valid():
            form9.save()
        else:
            context = {'form9': form9}
            return render(request, 'presupuesto/asignacion.html', context)
    presupuestoss = Presupuesto.objects.all()
    context = {'form9': PresupuestoForm(), 'presupuestoss': presupuestoss}
    return render(request, 'presupuesto/asignacion.html', context)

# VISTAS DE TRASPASOS
@login_required(login_url='login')
def traspasos(request):
    if request.method == 'POST':
        form9 = PresupuestoForm(request.POST)
        if form9.is_valid():
            form9.save()
        else:
            context = {'form9': form9}
            return render(request, 'presupuesto/traspasos.html', context)
    presupuestoss = Presupuesto.objects.all()
    context = {'form9': PresupuestoForm(), 'presupuestoss': presupuestoss}
    return render(request, 'presupuesto/traspasos.html', context)

# VISTAS DE PLANIFICACION
@login_required(login_url='login')
def planificacion(request):
            return render(request, 'planificacion/planificacion.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'gestion'])
def gestionh(request):
    if request.method == 'POST':
        form = GestionHForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context = {'form': form}
            return render(request, 'gestionhumana/gestion.html', context)
    gestionh = Personal.objects.all()
    context = {'form': GestionHForm(), 'formegh': GestionEHForm(), 'gestionh': gestionh}
    return render(request, 'gestionhumana/gestion.html', context)

# VISTAS DE POTENCIA
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'gestion'])
def potencia(request):
    if request.method == 'POST':
        formpi = IncidenciasForm(request.POST)
        if formpi.is_valid():
            formpi.save()
        else:
            context = {'formpi': formpi}
            return render(request, 'potencia/potencia.html', context)
    incidenciass = Incidencias.objects.all()
    context = {'formpi': IncidenciasForm(), 'formegh': IncidenciasEForm(), 'incidenciass': incidenciass}
    return render(request, 'potencia/potencia.html', context)

# VISTAS DE ACTUALIZACIÓN DE POTENCIA
def update_potencia(request, id):
    queryset = Incidencias.objects.get(id=id)
    form = IncidenciasEForm(instance=queryset)
    if request.method == 'POST':
        form = IncidenciasEForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/potencia#updatesuccess')

# VISTAS DE ELIMINACIÓN DE POTENCIA
def del_potencia(request, id):
    if request.method == 'POST':
        form = Incidencias.objects.get(id=id)
        form.delete()
        return redirect('/potencia#deletesuccess')

