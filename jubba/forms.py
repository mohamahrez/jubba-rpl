from django import forms
from .models import CostINfo


class CostINfoCreateForm(forms.ModelForm):
  class Meta:
    model = CostINfo
    fields = ("File_name","compny_name","town_city","phone", "text",)

