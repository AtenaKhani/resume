from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.urls import path

app_name = 'personal'

urlpatterns = [
    path('', views.dynamic_template_view, {'template_name': 'parent/base.html'}, name='start_page'),
    path('services/', views.dynamic_template_view, {'template_name': 'personal/services.html'}, name='services'),
    path('resume/', views.dynamic_template_view, {'template_name': 'personal/resume.html'}, name='resume'),
    path('about/', views. dynamic_template_view, {'template_name': 'personal/about.html'}, name='about'),
    path('portfolio/', views.dynamic_template_view, {'template_name': 'personal/portfolio.html'}, name='portfolio'),
    path('index/', views.dynamic_template_view, {'template_name': 'personal/index.html'}, name='index'),
    path('service-details/', views.dynamic_template_view, {'template_name': 'personal/service-details.html'},
         name='service-details'),
    path('portfolio-details/', views.dynamic_template_view, {'template_name': 'personal/portfolio-details.html'},
         name='portfolio-details'),
    path('contact/', views.contact, name='contact'),
]
