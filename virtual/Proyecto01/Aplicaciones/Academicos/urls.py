from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='cursos'),
    path('registrarcursos',views.registrarcursos),
    path('edicioncurso/<codigo>', views.edicioncurso),
    path('editarcurso', views.editarcurso),
    path('eliminarcursos/<codigo>',views.eliminarcursos),

    path('buscarcurso', views.buscarcurso, name= 'buscarcurso'),


    path('docentes',views.docente, name='docentes'),
    path('registrardocentes',views.registrardocentes),
    path('ediciondocente/<codigo>', views.ediciondocente),
    path('editardocente', views.editardocente),
    path('eliminardocente/<codigo>',views.eliminardocente),

    path('buscardocentes', views.buscardocentes, name= 'buscardocentes'),

    path('especialidad',views.especialidad, name='especialidad'),
    path('registrarespecialidad',views.registrarespecialidad),
    path('edicionespecialidad/<codigo>', views.edicionespecialidad),
    path('editarespecialidad', views.editarespecialidad),
    path('eliminarespecialidad/<codigo>',views.eliminarespecialidad),

    path('buscarespecialidad', views.buscarespecialidad, name= 'buscarespecialidad'),

]