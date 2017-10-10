from django.conf.urls import url, include
from . import views
from .views import BillingView
urlpatterns = [
    url(r'^dash', views.index, name="main"),
    url(r'^bill', BillingView.as_view()),
]
