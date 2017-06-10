from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='static_pages/header.html'), name='header'),
]
