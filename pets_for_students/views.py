from django.shortcuts import render
from pets_for_students.models import Cats, Students





# Create your views here.

def index(request):
    cats_list = Cats.objects.order_by('name')
    students_list = Students.objects.order_by('lastname')
    context_dict = {}
    context_dict['cats'] = cats_list
    context_dict['students'] = students_list

    return render(request, 'pets_for_students/index.html', context=context_dict )

def pets(request):
    cats_list = Cats.objects.order_by('name')
    context_dict = {}
    context_dict['cats'] = cats_list

    return render(request, 'pets_for_students/pets.html', context=context_dict)
