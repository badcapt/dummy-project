from django.conf.urls import url
from mydjangoapp import views

app_name = 'mydjangoapp'

urlpatterns = [url(r'^$',views.index, name ='index'),
                url(r'^help/$', views.help,name='help'),
                url(r'^user/$', views.users, name='user'),
                url(r'^form/$', views.form_view, name = 'form_page'),
                url(r'^info/$', views.info, name='info')
    ]
