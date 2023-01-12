
from django.urls import path

from . import views

urlpatterns = [
    path ('nuestros_perros/', views.list_our_dogs),
    path ('nuestros_voluntarios/' , views.list_our_volunteers),
    path ('nuestros_proyectos/' , views.list_Others_projects),
    path ('nuestras_instituciones_colaborativas/' , views.list_Our_collaborative_institutions),
    path ('nuevo_perro/' , views.create_our_dogs),
    path ('nuevo_voluntario/' , views.create_our_volunteers),
    path ('nuevo_proyecto/' , views.create_others_projects),
    path ('nueva_institucion_colaborativa' , views.create_our_collaborative_institutions)



]