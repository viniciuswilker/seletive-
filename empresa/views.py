from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def nova_empresa(request):
    if request.method == 'GET':
        return render(request,'nova_empresa.html')
    
    elif request.method == 'POST':
        pass