from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r"^api_view/", views.Validity_Api_1.as_view()),
]