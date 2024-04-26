from django.db import models

from account.models import CustomUser

# Create your models here.
class Subscription(models.Model):
  subscriber_name = models.CharField(max_length=300)
  subscription_plan = models.CharField(max_length=255)
  subscription_cost = models.CharField(max_length=255)
  
  # Paypal info
  paypal_subscription_id = models.CharField(max_length=300)
  is_active = models.BooleanField(default=False)
  
  # make sure user has one subscription
  user = models.OneToOneField(CustomUser, max_length=10, on_delete=models.CASCADE, unique=True)
  
  def __str__(self):
    return f'{self.subscriber_name} - {self.subscription_plan} subscription'