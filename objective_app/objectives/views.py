from django.shortcuts import render

from .models import Objectives

# Create your views here.

def index(request):
    objectives = Objectives.objects.all()
    return render(request,'objectives/index.html', {
        "objectives": objectives
    })
    
def objective_details(request, id):
    obj_detail = Objectives.objects.get(id=id)
    return render(request,'objectives/objective_details.html', {"obj_detail": obj_detail})    