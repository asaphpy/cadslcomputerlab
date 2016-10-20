from django.contrib import admin
from .models import Service, about, price, Last_work


class ServiceAdmin(admin.ModelAdmin):
	list_display = ['name']
admin.site.register(Service, ServiceAdmin)

class AboutAdmin(admin.ModelAdmin):
	list_display = ['name']
admin.site.register(about, AboutAdmin)

class PriceAdmin(admin.ModelAdmin):
	list_display = ['title']

admin.site.register(price, PriceAdmin)

class Last_workAdmin(admin.ModelAdmin):
	list_display = ['name']
admin.site.register(Last_work, Last_workAdmin)
