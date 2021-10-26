from django.shortcuts import render,redirect
from django.http import Http404
from django.urls import reverse
from django.views.generic import ListView,TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import CostINfo
from .forms import CostINfoCreateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout





# Create your views here.
'''class SignUp(LoginRequiredMixin,CreateView):
      form_class = UserCreationForm
      success_url = reverse_lazy("login")   
      template_name = "registration/signup.html"'''

@login_required
def home(request):
  return render(request, "order/home.html")

'''class OrderList(LoginRequiredMixin,ListView):
     template_name = 'order/orders_list.html'
     queryset = Orders.objects.all()
'''
class OrderCreate(LoginRequiredMixin,CreateView):
   model = CostINfo
   template_name = 'order/order_create_form.html'
   form_class = CostINfoCreateForm

class OrderDelete(LoginRequiredMixin, DeleteView):
    model = CostINfo
    template_name = "order/order_delete_form.html"
    success_url = "/order/list"
'''
class CostomerCreate(CreateView):
   model = Costomer
   template_name = 'order/Costomer_create_form.html'
   form_class = CostomerCreateForm
'''
class CostomerList(LoginRequiredMixin,ListView):
     template_name = 'order/costomer_list.html'
     queryset = CostINfo.objects.all()

class Report(LoginRequiredMixin,ListView):
     template_name = 'order/Report.html'
     queryset = CostINfo.objects.all()
'''
class CostomerDelete(LoginRequiredMixin, DeleteView):
    model = Orders
    template_name = "order/costomer_delete_form.html"
    success_url = "/costomer/list"
'''
class WorkUpdateView(UpdateView):
    model = CostINfo
    fields = ["File_name","compny_name","text"]
    template_name = 'order/costinfo_update_form.html'
    success_url = "/order/list"

class OrderList(LoginRequiredMixin,ListView):
     template_name = 'order/orders_list.html'
     queryset = CostINfo.objects.all()
     
def logout_request(request):
  logout(request)
  return redirect("home")
