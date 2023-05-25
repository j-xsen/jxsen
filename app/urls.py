from django.urls import path
from django.views.generic import TemplateView
from django.urls import path, include


from . import views


urlpatterns = [
    path('', views.index),
    path('epk', views.epk, name='epk'),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
]

