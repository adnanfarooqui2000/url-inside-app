from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse,JsonResponse

def home(request):
    return HttpResponse("<center><h1 style='color : purple'>Welcome to App 1 page of django </h1></center`>")
data={
"Name":"Adnan Farooqui"
"Age" "23"
}
def register(request):
    return render(request,'register.html')