from django.shortcuts import render

# Create your views here.
def display(request):
    return render(request,'temp_myapp/temp1.html')