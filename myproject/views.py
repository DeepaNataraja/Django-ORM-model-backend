from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import DemoForm

def form_view(request):
    form ={"DemoForm"}
    context ={"form":form}
    return render(request,"demo.html",context)