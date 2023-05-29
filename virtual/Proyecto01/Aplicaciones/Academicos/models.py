from django.db import models

# Create your models here.

class Especialidad(models.Model):
    idEspecialidad = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Docente(models.Model):
    idDocente = models.CharField(primary_key=True, max_length=6)
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    fecha_ingreso = models.DateField()
    dni = models.IntegerField()
    telefono = models.IntegerField()

    def __str__(self):
        return self.apellido

class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    idAlumno = models.CharField(primary_key= True,max_length = 6)
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    dni = models.IntegerField()
    fecha_nacimiento = models.DateField()
    telefono = models.IntegerField()
    
    def __str__(self):
        return self.nombre




  

