from django.conf.urls import include, url
from . import views

urlpatterns = [
    
    url(r'^$', views.start, name='sb_admin_start'),
    url(r'^dashboard/$', views.dashboard, name='sb_admin_dashboard'),
    url(r'^charts/$', views.charts, name='sb_admin_charts'),
    url(r'^tables/$', views.tables, name='sb_admin_tables'),
    url(r'^forms/$', views.forms, name='sb_admin_forms'),
    url(r'^bootstrap-elements/$', views.bootstrap_elements, name='sb_admin_bootstrap_elements'),
    url(r'^bootstrap-grid/$', views.bootstrap_grid, name='sb_admin_bootstrap_grid'),
    url(r'^rtl-dashboard/$', views.rtl_dashboard, name='sb_admin_rtl_dashboard'),
    url(r'^blank/$', views.blank, name='sb_admin_blank'),
]
