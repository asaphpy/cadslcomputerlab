from django.db import models

class ServiceManager(models.Manager):
	def search(self, query):
		return self.get_queryset().filter(
			models.Q(name__icontains=query)
	)

class AboutManager(models.Manager):
	def search(self, query):
		return self.get_queryset().filter(
			models.Q(name__icontains=query)
	)

class WorkManager(models.Manager):
	def search(self, query):
		return self.get_queryset().filter(
			models.Q(name__icontains=query)
	)

class Service(models.Model):
	name = models.CharField('Nome', max_length=100)
	description = models.TextField('Descrição', blank=False)
	image = models.ImageField(
		upload_to='services/images', verbose_name='Imagem'
	)
	objects = ServiceManager()	

class about(models.Model):
	name = models.CharField('Nome', max_length=100)
	description = models.TextField('Sobre Nós', blank=False)
	image = models.ImageField(
		upload_to='about_to/images', verbose_name='Imagem'
	)
	about_objects = AboutManager()	

class price(models.Model):
	price_basic = models.CharField('Preço', max_length=100)
	title = models.CharField('Descrição', blank=False, max_length=100)
	categories = models.TextField('Lista de Serviços')

class Last_work(models.Model):
	name = models.CharField('Nome', max_length=100)
	description = models.TextField('Descrição', blank=False)
	image = models.ImageField(
		upload_to = 'last_work_to/images', verbose_name='Imagem'
	)
	work_objects = WorkManager()