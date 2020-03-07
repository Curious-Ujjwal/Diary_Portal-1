from django.conf.urls import url,include
from . import views
urlpatterns = [

    url(r'^$',views.getmainpage,name='main_page'),
    url(r'^placement/remarks/(?P<pk>\d+)/$', views.getremarks, name='premarks'),
    url(r'^intern/remarks/(?P<pk>\d+)/$', views.getremarks, name='iremarks'),
    url(r'placement/$', views.getPlacement,name='placement'),
    url(r'intern/$', views.getIntern, name='intern'),
    url(r'^intern/(?P<pk>\d+)/$', views.save_changes_view, name='intern_company_edit'),
    url(r'^placement/(?P<pk>\d+)/$', views.save_changes_view, name='placement_company_edit'),
    url(r'placement_add_company/$', views.add_placement_company, name='placement_add_company'),
    url(r'intern_add_company/$', views.add_intern_company, name='intern_add_company'),
 	url(r'placement/search/$', views.searchPlacement, name='search'),
    url(r'intern/search/$', views.searchIntern, name='search'),
    url(r'placement/authentication/$',views.Placement_Authenticate,name='Placement_Authenticate'),
    url(r'intern/authentication/$', views.Intern_Authenticate, name='Intern_Authenticate'),
    url(r'placement/edit_ID/$', views.edit_Placement_ID, name='edit_Placement_ID'),
    url(r'intern/edit_ID/$', views.edit_Intern_ID, name='edit_Intern_ID')

]