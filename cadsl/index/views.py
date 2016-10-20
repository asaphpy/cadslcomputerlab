from django.shortcuts import render

from .models import Service, about, Last_work

def home(request):
	services = Service.objects.all()
	abouts = about.about_objects.all()
	last_works = Last_work.work_objects.all()
	template_name = 'index/index.html'
	context = {
		'services': services,
		'abouts': abouts,
		'last_works': last_works
	}
	return render(request, template_name, context)