from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            CursoListado = Curso.objects.order_by('codigo')
            return render(request, 'GestionCursos.html', {"cursos":CursoListado}) 
        else:
            # El usuario no ha proporcionado credenciales válidas
            pass
    return render(request,'Login.html')

# Create your views here.

def home(request):
    cursosListado = Curso.objects.all()
    return render(request, "GestionCursos.html",{"cursos":cursosListado})

def registrarcursos(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    creditos = request.POST["numcreditos"]

    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect('/')

def edicioncurso(request, codigo):
    curso = Curso.objects.get(codigo = codigo)
    return render(request, "EdicionCursos.html",{"curso":curso})

def editarcurso(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    creditos = request.POST["numcreditos"]

    curso = Curso.objects.get(codigo = codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    return redirect('/')

def eliminarcursos(request,codigo):
    curso = Curso.objects.get(codigo = codigo)
    curso.delete()
    return redirect('/')

def buscarcurso(request):
    if request.method == "POST":
        buscarnombre = request.POST.get('nombre')
        busqueda=Curso.objects.filter(nombre__icontains=buscarnombre)
        return render(request,'BuscarCursos.html',{"data":busqueda})
    else:
        cursosListado = Curso.objects.all()
        return render(request, "BuscarCursos.html",{"data":cursosListado})





def docente(request):
    docentesListado = Docente.objects.all()
    return render(request, "GestionDocentes.html",{"docentes":docentesListado})

def registrardocentes(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    fecha_ingreso = request.POST["txtfecha_ingreso"]
    dni = request.POST["numdni"]
    telefono = request.POST["numtelefono"]

    docente = Docente.objects.create(idDocente=codigo, nombre=nombre, apellido=apellido, fecha_ingreso = fecha_ingreso, dni = dni, telefono = telefono)
    return redirect('/docentes')

def ediciondocente(request, codigo):
    docente = Docente.objects.get(idDocente = codigo)
    return render(request, "EdicionDocentes.html",{"docente":docente})

def editardocente(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    fecha_ingreso = request.POST["txtfecha_ingreso"]
    dni = request.POST["numdni"]
    telefono = request.POST["numtelefono"]

    docente = Docente.objects.get(idDocente = codigo)
    docente.nombre = nombre
    docente.apellido = apellido
    docente.fecha_ingreso = fecha_ingreso
    docente.dni = dni
    docente.telefono = telefono
    docente.save()

    return redirect('/docentes')

def eliminardocente(request,codigo):
    docente = Docente.objects.get(idDocente = codigo)
    docente.delete()
    return redirect('/docentes')

def buscardocentes(request):
    if request.method == "POST":
        buscarfecha_ingreso = request.POST.get('fecha_ingreso')
        busqueda=Docente.objects.filter(fecha_ingreso__icontains=buscarfecha_ingreso)
        return render(request,'BuscarDocentes.html',{"data":busqueda})
    else:
        docentesListado = Docente.objects.all()
        return render(request, "BuscarDocentes.html",{"data":docentesListado})






def especialidad(request):
    especialidadListado = Especialidad.objects.all()
    return render(request, "GestionEspecialidad.html",{"especialidad":especialidadListado})

def registrarespecialidad(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]

    especialidad = Especialidad.objects.create(idEspecialidad=codigo, nombre=nombre, descripcion=descripcion)
    return redirect('/especialidad')

def edicionespecialidad(request, codigo):
    especialidad = Especialidad.objects.get(idEspecialidad = codigo)
    return render(request, "EdicionEspecialidad.html",{"especialidad":especialidad})

def editarespecialidad(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]

    docente = Especialidad.objects.get(idEspecialidad = codigo)
    docente.nombre = nombre
    docente.descripcion = descripcion
    docente.save()

    return redirect('/especialidad')

def eliminarespecialidad(request,codigo):
    especialidad = Especialidad.objects.get(idEspecialidad = codigo)
    especialidad.delete()
    return redirect('/especialidad')

def buscarespecialidad(request):
    if request.method == "POST":
        buscarnombre = request.POST.get('nombre')
        busqueda=Especialidad.objects.filter(nombre__icontains=buscarnombre)
        return render(request,'BuscarCursos.html',{"data":busqueda})
    else:
        especialidadListado = Especialidad.objects.all()
        return render(request, "BuscarEspecialidad.html",{"data":especialidadListado})
    



def alumno(request):
    alumnosListado = Alumno.objects.all()
    return render(request, "GestionAlumnos.html",{"alumnos":alumnosListado})

def registraralumnos(request):
    codigo = request.POST["txtcodigo"]
    apellido = request.POST["txtapellido"]
    nombre = request.POST["txtnombre"]
    dni = request.POST["numdni"]
    fecha_nacimiento = request.POST["txtfecha_nacimiento"]
    telefono = request.POST["numtelefono"]

    alumnos = Alumno.objects.create(idAlumno=codigo, nombre=nombre, apellido=apellido, fecha_nacimiento = fecha_nacimiento, dni = dni, telefono = telefono)
    return redirect('/alumnos')

def buscaralumnos(request):
    if request.method == "POST":
        buscarnombre = request.POST.get('nombre')
        busqueda=Alumno.objects.filter(nombre__icontains=buscarnombre)
        return render(request,'BuscarAlumnos.html',{"data":busqueda})
    else:
        alumnosListado = Alumno.objects.all()
        return render(request, "BuscarAlumnos.html",{"data":alumnosListado})
    
def edicionalumno(request, codigo):
    alumno = Alumno.objects.get(idAlumno = codigo)
    return render(request, "EdicionAlumnos.html",{"alumno":alumno})
    
def editaralumno(request):
    codigo = request.POST["txtcodigo"]
    apellido = request.POST["txtapellido"]
    nombre = request.POST["txtnombre"]
    dni = request.POST["numdni"]
    fecha_nacimiento = request.POST["txtfecha_nacimiento"]
    telefono = request.POST["numtelefono"]

    alumno = Alumno.objects.get(idAlumno = codigo)
    alumno.nombre = nombre
    alumno.apellido = apellido
    alumno.fecha_nacimiento = fecha_nacimiento
    alumno.dni = dni
    alumno.telefono = telefono
    alumno.save()

    return redirect('/alumnos')

def eliminaralumno(request,codigo):
    alumno = Alumno.objects.get(idAlumno = codigo)
    alumno.delete()
    return redirect('/alumnos')


