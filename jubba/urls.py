from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("account/", include("django.contrib.auth.urls")),
    path("logout/", views.logout_request, name="logout"),
    path("order/create", views.OrderCreate.as_view(), name="ordercreate"),
    path("costomer/list", views.CostomerList.as_view(), name="costomerlist"), 
    path("Report/", views.Report.as_view(), name="Report"),

    ]
