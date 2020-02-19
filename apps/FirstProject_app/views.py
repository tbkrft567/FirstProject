from django.shortcuts import render, redirect


def index(request):
   context={
      "test": "this works"
   }
   return  render(request, "FirstProject_app/index.html", context)

# Create your views here.
