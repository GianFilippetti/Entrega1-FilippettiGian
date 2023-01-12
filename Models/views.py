from django.shortcuts import render
from django.http import HttpResponse
from Models.models import Our_dogs , Our_volunteers , Our_collaborative_institutions , Others_projects
from Models.forms import Our_dogs_forms , Our_volunteers_forms , Our_collaborative_institutions_forms , Others_projects_forms
# Create your views here.

def create_our_dogs (request):
    if request.method == 'GET':
        context = {
            'dog_form' : Our_dogs_forms ()
        }
        return render (request , 'create_our_dogs.html' , context = context)
    elif request.method == 'POST':
        dog_form = Our_dogs_forms (request.POST)
        if dog_form.is_valid ():
            Our_dogs.objects.create (
                dog_name = dog_form.cleaned_data ['dog_name'],
                dog_age = dog_form.cleaned_data ['dog_age'],
                dog_history= dog_form.cleaned_data ['dog_history'],
                dog_status = dog_form.cleaned_data ['dog_status']
                )
            context = {
                'message' : 'Se agrego el nuevo perro'
            }
            return render ( request , 'create_our_dogs.html' , context = context)
        else:
            context = {
                'dog_form_errors': dog_form.errors ,
                'dog_form' : Our_dogs_forms ()
            }
            return render ( request , 'create_our_dogs.html' , context = context)

def create_our_volunteers (request):
    if request.method == 'GET':
        context = {
            'volunteer_form' : Our_volunteers_forms ()
        }
        return render (request , 'create_our_volunteer.html' , context = context)
    elif request.method == 'POST':
        volunteer_form = Our_volunteers_forms (request.POST)
        if volunteer_form.is_valid ():
            Our_volunteers.objects.create (
                volunteer_name = volunteer_form.cleaned_data ['volunteer_name'],
                volunteer_age = volunteer_form.cleaned_data ['volunteer_age'],
                volunteer_reason_to_be_a_volunteer = volunteer_form.cleaned_data ['volunteer_reason_to_be_a_volunteer'],
                volunteer_favourite_dog_and_reason = volunteer_form.cleaned_data ['volunteer_favourite_dog_and_reason']
            )
            context = {
                'message' : 'Se agrego el nuevo voluntario'
            }
            return render ( request , 'create_our_volunteer.html' , context = context)
        else:
            context = {
                'volunteer_form_errors': volunteer_form.errors ,
                'volunteer_form' : Our_volunteers_forms ()
            }
            return render ( request , 'create_our_volunteer.html' , context = context)

def create_our_collaborative_institutions (request):
    if request.method == 'GET':
        context = {
            'colaborative_institution_form' : Our_collaborative_institutions_forms ()
        }
        return render (request , 'create_our_colaborative_institution.html' , context = context)
    elif request.method == 'POST':
        colaborative_institution_form = Our_collaborative_institutions_forms (request.POST)
        if colaborative_institution_form.is_valid ():
            Our_collaborative_institutions.objects.create (
                instituion_name = colaborative_institution_form.cleaned_data ['instituion_name'],
                institution_reason_to_colaborate = colaborative_institution_form.cleaned_data ['institution_reason_to_colaborate'],
                institution_vision_of_animals= colaborative_institution_form.cleaned_data ['institution_vision_of_animals'],
            )
            context = {
                'message' : 'Se agrego la nueva institucion colaborativa'
            }
            return render ( request , 'create_our_colaborative_institution.html' , context = context)
    else:
            context = {
                'colaborative_institution_errors': colaborative_institution_form.errors ,
                'colaborative_institution_form' : Our_collaborative_institutions_forms ()
            }
            return render ( request , 'create_our_colaborative_institution.html', context = context)

def create_others_projects (request):
    if request.method == 'GET':
        context = {
            'others_projects_form' : Others_projects_forms ()
        }
        return render (request , 'create_others_projects.html' , context = context)
    elif request.method == 'POST':
        others_projects_form = Others_projects_forms (request.POST)
        if others_projects_form.is_valid ():
            Others_projects.objects.create (
                project_name = others_projects_form.cleaned_data ['project_name'],
                institution_or_person_in_charge = others_projects_form.cleaned_data ['institution_or_person_in_charge'],
                project_objective= others_projects_form.cleaned_data ['project_objective'],
            )
            context = {
                'message' : 'Se agrego el nuevo proyecto'
            }
            return render ( request , 'create_others_projects.html' , context = context)
        else:
            context = {
                'others_projects_form_errors': others_projects_form.errors ,
                'others_projects_form'  : Others_projects_forms ()
            }
            return render ( request , 'create_others_projects.html' , context = context)

def list_our_dogs (request):
    all_dogs = Our_dogs.objects.all 
    context = {
        'our_dogs': all_dogs
    }
    return render (request ,'list_our_dogs.html', context = context )

def list_our_volunteers (request):
    all_volunteers = Our_volunteers.objects.all 
    print (all_volunteers)
    context = {
        'our_volunteers': all_volunteers,
    }
    return render (request ,'list_our_volunteers.html', context = context )

def list_Our_collaborative_institutions(request):
    all_institutions = Our_collaborative_institutions.objects.all 
    print (all_institutions)
    context = {
        'our_collaborative_institutions': all_institutions,
    }
    return render (request ,'list_our_colaborative_institutions_list.html', context = context)

def list_Others_projects (request):
    all_projects = Others_projects.objects.all ()
    print (all_projects)
    context = {
        'others_projects': all_projects,
    }
    return render (request ,'list_others_projects.html', context = context )
