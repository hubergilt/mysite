from django.shortcuts import render
from django.apps import apps

def index(request):
	template = "admin/index.html"
	context = {"app_list": apps.get_app_configs()}
	return render(request, template, context)