from django.http import request
from django.shortcuts import render_to_response

def home(request):
    return render_to_response(template_name='index.html')