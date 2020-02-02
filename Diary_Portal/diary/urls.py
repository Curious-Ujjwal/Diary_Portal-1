from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^$',views.gethomepage,name='diary_home'),
    url(r'(?P<pk>\d+)/$', views.getremarks, name='remarks'),

]