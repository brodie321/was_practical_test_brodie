from django.shortcuts import render




# Create your views here.

def index(request):
    return render(request, 'pets_for_students/index.html')

def pets(request):
    return render(request, 'pets_for_students/pets.html')
