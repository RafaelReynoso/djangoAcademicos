# Generated by Django 4.2.1 on 2023-05-29 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academicos', '0003_remove_curso_docente_remove_curso_especialidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('idAlumno', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('apellido', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('dni', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.IntegerField()),
            ],
        ),
    ]
