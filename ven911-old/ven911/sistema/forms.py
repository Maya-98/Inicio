from django import forms
from sistema.models import Reglamentos, Normativas, Entradap, Salidap, Gestion, UserC, Departamentos, Sedes, Vehiculos, Presupuesto, Personal, Incidencias

# FORMULARIO DE CREACIÓN DE USUARIOS - ADMIN
class UserCreateForm(forms.ModelForm):
    class Meta:
        model = UserC
        fields = ('username', 'password', 'nombre', 'apellido', 'tipo', 'departamento', 'sede')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

# FORMULARIO DE ACTUALIZACIÓN DE USUARIOS - ADMIN
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserC
        fields = ('username', 'nombre', 'apellido', 'tipo', 'departamento', 'sede')

# FORMULARIO DE ACTUALIZACIÓN DE PASSWORD USUARIOS - ADMIN
class UserUpdatePForm(forms.ModelForm):
    class Meta:
        model = UserC
        fields = ('password',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

# FORMULARIO DE CREACIÓN DE DEPARTAMENTOS - ADMIN
class DepartamentosForm(forms.ModelForm):
    class Meta:
        model = Departamentos
        fields = ('name',)

# FORMULARIO DE ACTUALIZACIÓN DE DEPARTAMENTOS - ADMIN
class DepartamentosEForm(forms.ModelForm):
    class Meta:
        model = Departamentos
        fields = ('name',)
        
# FORMULARIO DE CREACIÓN DE SEDES - ADMIN
class SedesForm(forms.ModelForm):
    class Meta:
        model = Sedes
        fields = ('name',)

# FORMULARIO DE ACTUALIZACIÓN DE SEDES - ADMIN
class SedesEForm(forms.ModelForm):
    class Meta:
        model = Sedes
        fields = ('name',)

# FORMULARIO DE REGLAMENTOS
class ReglamentsForm(forms.ModelForm):
    date = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Reglamentos
        fields = ('name', 'file', 'user', 'date')

# FORMULARIO DE ACTUALIZACIÓN DE REGLAMENTOS
class ReglamentsUForm(forms.ModelForm):
    date = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Reglamentos
        fields = ('name', 'user', 'date')

# FORMULARIO DE ACTUALIZACIÓN DE ARCHIVO REGLAMENTOS
class ReglamentsUFForm(forms.ModelForm):
    class Meta:
        model = Reglamentos
        fields = ('file',)

# FORMULARIO DE NORMATIVAS
class NormativasForm(forms.ModelForm):
    date = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Normativas
        fields = ('name', 'file', 'user', 'date')

# FORMULARIO DE ACTUALIZACIÓN NORMATIVAS
class NormativasUForm(forms.ModelForm):
    date = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Normativas
        fields = ('name', 'user', 'date')

# FORMULARIO DE ACTUALIZACIÓN DE ARCHIVOS NORMATIVAS
class NormativasUFForm(forms.ModelForm):
    class Meta:
        model = Normativas
        fields = ('file',)

# FORMULARIO DE ENTRADA PERSONAL
class EntradapForm(forms.ModelForm):
    fecha = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    hora = forms.CharField(widget=forms.TextInput(attrs={'type':'time'}))
    class Meta:
        model = Entradap
        fields = ('name', 'apellido', 'cedula', 'telefono', 'fecha', 'direccion', 'cargo', 'hora')

# FORMULARIO DE ACTUALIZACIÓN ENTRADA PERSONAL
class EntradapEForm(forms.ModelForm):
    fecha = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    hora = forms.CharField(widget=forms.TextInput(attrs={'type':'time'}))
    class Meta:
        model = Entradap
        fields = ('name', 'apellido', 'cedula', 'telefono', 'fecha', 'direccion', 'cargo', 'hora')

# FORMULARIO DE SALIDA PERSONAL
class SalidapForm(forms.ModelForm):
    fecha = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    hora = forms.CharField(widget=forms.TextInput(attrs={'type':'time'}))
    class Meta:
        model = Salidap
        fields = ('name', 'apellido', 'cedula', 'telefono', 'fecha', 'direccion', 'cargo', 'hora')

# FORMULARIO DE ACTUALIZACIÓN SALIDA PERSONAL
class SalidapEForm(forms.ModelForm):
    fecha = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    hora = forms.CharField(widget=forms.TextInput(attrs={'type':'time'}))
    class Meta:
        model = Salidap
        fields = ('name', 'apellido', 'cedula', 'telefono', 'fecha', 'direccion', 'cargo', 'hora')

# FORMULARIO DE GESTIÓN DE INCIDENTES
class GestionForm(forms.ModelForm):
    fecha = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    hora = forms.CharField(widget=forms.TextInput(attrs={'type':'time'}))
    class Meta:
        model = Gestion
        fields = ('name', 'apellido', 'cedula',  'tipo', 'descripcion', 'fecha', 'direccion', 'cargo', 'hora')

# FORMULARIO DE ACTUALIZACIÓN GESTIÓN DE INCIDENTES
class GestionEForm(forms.ModelForm):
    fecha = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    hora = forms.CharField(widget=forms.TextInput(attrs={'type':'time'}))
    class Meta:
        model = Gestion
        fields = ('name', 'apellido', 'cedula', 'tipo', 'descripcion', 'fecha', 'direccion', 'cargo', 'hora')

# FORMULARIO DE VEHÍCULOS
class VehiculosForm(forms.ModelForm):
    fecha = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    hora = forms.CharField(widget=forms.TextInput(attrs={'type':'time'}))
    class Meta:
        model = Vehiculos
        fields = ('nombre', 'apellido', 'cedula', 'tipo','transporte', 'modelo', 'placa', 'fecha', 'hora')

# FORMULARIO DE ACTUALIZACIÓN VEHÍCULOS
class VehiculosEForm(forms.ModelForm):
    fecha = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    hora = forms.CharField(widget=forms.TextInput(attrs={'type':'time'}))
    class Meta:
        model = Vehiculos
        fields = ('nombre', 'apellido', 'cedula', 'tipo', 'transporte', 'modelo', 'placa', 'fecha', 'hora')

# FORMULARIO DE PRESUPUESTO
class PresupuestoForm(forms.ModelForm):
    fechai = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    fechac = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Presupuesto
        fields = ('nombrep', 'fechai', 'fechac', 'situacionp', 'pplurianual', 'montoaño', 'montoproyecto', 'responsableg', 'responsablet', 'responsabler', 'responsablea', 'estatus')

# FORMULARIO DE ACTUALIZACIÓN DE PRESUPUESTO
class PresupuestoEForm(forms.ModelForm):
    fechai = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    fechac = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Presupuesto
        fields = ('nombrep', 'fechai', 'fechac', 'situacionp', 'pplurianual', 'montoaño', 'montoproyecto', 'responsableg', 'responsablet', 'responsabler', 'responsablea', 'estatus')

# FORMULARIO DE GESTIÓN HUMANA
class GestionHForm(forms.ModelForm):
    fecha_nac = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    fechac = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Personal
        fields = ('nombre', 'apellido', 'cedula', 'nacionalidad', 'sexo', 'fecha_nac', 'edad', 'telefono', 'estado_civil', 'conyugue', 'cedula_conyugue', 'tipo_sangre', 'discapacitado', 'talla_camisa', 'talla_pantalon', 'talla_zapato', 'fasmij', 'direccion', 'nro_cuenta', 'email', 'grado_instruccion', 'estudias', 'comision_servicio', 'pnb', 'tipo_personal', 'cargo', 'fecha_ingreso_911', 'fecha_ingreso_apn', 'contratos', 'departamento', 'hijos_13_18', 'edades1', 'niño_menor_12', 'edades2', 'niña_menor_12', 'edades3', 'hijos_discapacidad', 'edades4', 'sede')

# FORMULARIO DE ACTUALIZACIÓN GESTIÓN HUMANA
class GestionEHForm(forms.ModelForm):
    fecha_nac = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    fechac = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Personal
        fields = ('nombre', 'apellido', 'cedula', 'nacionalidad', 'sexo', 'fecha_nac', 'edad', 'telefono', 'estado_civil', 'conyugue', 'cedula_conyugue', 'tipo_sangre', 'discapacitado', 'talla_camisa', 'talla_pantalon', 'talla_zapato', 'fasmij', 'direccion', 'nro_cuenta', 'email', 'grado_instruccion', 'estudias', 'comision_servicio', 'pnb', 'tipo_personal', 'cargo', 'fecha_ingreso_911', 'fecha_ingreso_apn', 'contratos', 'departamento', 'hijos_13_18', 'edades1', 'niño_menor_12', 'edades2', 'niña_menor_12', 'edades3', 'hijos_discapacidad', 'edades4', 'sede')

# FORMULARIO DE INCIDENCIAS
class IncidenciasForm(forms.ModelForm):
    class Meta:
        model = Incidencias
        fields = ('estado', 'sede', 'departamento', 'tipoincidencia', 'usuario', 'observaciones')

# FORMULARIO DE ACTUALIZACIÓN DE INCIDENCIAS
class IncidenciasEForm(forms.ModelForm):
    class Meta:
        model = Incidencias
        fields = ('estado', 'sede', 'departamento', 'tipoincidencia', 'usuario', 'observaciones')