from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from rango import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^rango/', include('rango.urls')),
	# The above maps any urls that start with rango/ to
	#be handled by the rango app
    url(r'^admin/', admin.site.urls),
]
