from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
def json_view(request):
    return JsonResponse({"Name": "Hello World!"})