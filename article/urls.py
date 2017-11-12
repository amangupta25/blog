from django.conf.urls import url
from . import views

app_name = 'article'

urlpatterns = [
	url(r'^$', views.hello, name='hello'),

	]