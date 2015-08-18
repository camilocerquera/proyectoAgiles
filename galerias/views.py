from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime
from django.core.mail import EmailMessage



from .models import Urls,UrlsForm,Contact,ContactForm

#Se define la funcionalidad del Home
def index(request):
	#Se crea la variable de arrays
	tabla_urls=[]
	#Se cargan todos los registros de la tabla Ulrs ordenados por fecha mas reciente
	tabla_urls=Urls.objects.all().order_by('-date');
	#La informacion recuperada es enviada a la pantalla
	return render_to_response('index.html',{'galerias':tabla_urls,'request':request},context_instance=RequestContext(request))

#Se define la funcionalidad de la pantalla de Adicionar imagenes
def add(request):
	#Variable de mesaje de error o exito
	msj=''
	if request.method == 'POST':
		form=UrlsForm(request.POST)
		#se valida que el formulario este bien diligenciao
		if form.is_valid():
			#Se recuperan los datos ingresados en el formulario
			url = form.cleaned_data['url']
			description = form.cleaned_data['description']
			title = form.cleaned_data['title']
			now = datetime.datetime.now()
			user = 'anonimo'
			#Se realiza una validacion de campos obligatorios
			if (url !='' and title !='' and description != ''):
				#Se guarda la imagen cargada
				urlObject = Urls(url=url, user=user, date=now, title=title, description=description)
				urlObject.save()
				msj='Foto agregada exitosamente'
			else:
				msj='Informacion Incompleta'
		else:
			msj='La informacion esta incompleta'
		
	else:
		form=UrlsForm()
	#Se retorna la respuesta a la pantalla
	return render_to_response('add.html',{'form':form,'msj':msj,'request':request},context_instance=RequestContext(request))



#Se define la funcionalidad de la pantalla de Acerca de..
def about(request):
	return render_to_response('about.html',context_instance=RequestContext(request))

#Se define la funcionalidad de la pantalla de contacto
def contact(request):
	#Variable de mesaje de error o exito
	msj=''
	if request.method == 'POST':
		form=ContactForm(request.POST)
		#Se valida la informacion ingresada en el formulario
		if form.is_valid():
			#Se obtiene la informacion diligenciada en el formulario
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			msg = form.cleaned_data['msg']
			now = datetime.datetime.now()
			#Se verifican campo obligatorios
			if (name !='' and email !='' and msg != ''):
				#Se guarda un registro de la solicitud de contacto
				contactObject = Contact(name=name, email=email, msg=msg, date=now)
				contactObject.save()
				#Se envia el mensaje de contacto al correo de la aplicacion
				#Tambien se envia una copia del mensaje al correo del solicitante
				email = EmailMessage('Galeria de Imagenes', name + ' envia el mensaje: ' + msg, to=[email,'procesosagiles2015@gmail.com'])
				email.send()

				msj='El mensaje a sido enviado'
			else:
				msj='Informacion Incompleta'
		else:
			msj='La informacion esta incompleta'
		
	else:
		form=ContactForm()
	#Se retorna a la pantalla
	return render_to_response('contact.html',{'form':form,'msj':msj,'request':request},context_instance=RequestContext(request))
