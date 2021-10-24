from django.db import models

# Create your models here.
class CostINfo(models.Model):
  Paid = 'PAID'
  Unpaid = 'UNPAID'
  PAYMENT_CHOICE = [
        (Paid, 'PAID'),
        (Unpaid, 'UNPAID'),
  ]
  created_at = models.DateTimeField(auto_now_add=True)
  File_name = models.CharField(max_length=30)
  compny_name = models.CharField(max_length=30)
  town_city = models.CharField(max_length=30)
  phone = models.CharField(max_length=30)
  text = models.TextField(max_length=300) 
 #pdf = models.FileField(null=True, blank=True)
 # Rest = models.IntegerField(max_length=30)
  '''Payment_choice = models.CharField(
        max_length=10,
        choices=PAYMENT_CHOICE,
    )
''' 
  def get_absolute_url(self):
      return list
