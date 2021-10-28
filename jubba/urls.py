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
    path("order/list", views.OrderList.as_view(), name="orderlist"),
    path('order/delete/<pk>', views.OrderDelete.as_view(), name="orderdelete"),
    path('order/update/<pk>', views.WorkUpdateView.as_view(), name="orderupdate"),
        path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='registration/change-password.html',
            success_url = '/'
        ),
        name='change_password'
    ),
    ]
