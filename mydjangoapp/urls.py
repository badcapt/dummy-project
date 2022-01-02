from django.conf.urls import url
from mydjangoapp import views

urlpatterns = [url(r'^$',views.info,name ='info')]
