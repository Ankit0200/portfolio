from django.shortcuts import render

from .models import TECH_KNOWLEDGE,Project




# Create your views here.
def index(request):
    total_tech_stack=TECH_KNOWLEDGE.objects.all()
    total_projects=Project.objects.all()
    return render(request, 'index.html',{'total_tech_stack':total_tech_stack,'total_projects':total_projects})
