from django import forms

class Our_dogs_forms (forms.Form):
    dog_name = forms.CharField (max_length=30)
    dog_age = forms.IntegerField ()
    dog_history = forms.CharField (max_length=500)
    dog_status = forms.BooleanField(required=False)

class Our_volunteers_forms (forms.Form):
    volunteer_name = forms.CharField (max_length=30)
    volunteer_age = forms.IntegerField ()
    volunteer_reason_to_be_a_volunteer = forms.CharField(max_length=500)
    volunteer_favourite_dog_and_reason = forms.CharField(max_length=500)

class Our_collaborative_institutions_forms (forms.Form):
    instituion_name = forms.CharField (max_length=30)
    institution_reason_to_colaborate = forms.CharField (max_length=500)
    institution_vision_of_animals = forms.CharField (max_length=500)

class Others_projects_forms (forms.Form):
    project_name = forms.CharField(max_length=30)
    institution_or_person_in_charge = forms.CharField (max_length=30)
    project_objective = forms.CharField (max_length =500)



