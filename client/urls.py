from django.urls import path 
from . import views

urlpatterns = [
    path('client-dashboard', views.client_dashboard, name="client-dashboard"),
    path('browse-articles', views.browse_articles, name="browse-articles"),
    path('subscription-locked', views.subscription_locked, name="subscription-locked"),
    path('subscription-plans', views.subscription_plans, name="subscription-plans"),
    path('account-manangement-client', views.account_management,                    name="account-manangement-client"),
    # notice there are two <> in the route below for create-subscription
    # Subscription urls
    path('create-subscription/<subID>/<plan>', views.create_subscription,name="create-subscription"),
    path('delete-subscription/<subID>', views.delete_subscription, name="delete-subscription"),
    path('update-subscription/<subID>', views.update_subscription, name="update-subscription"),
    path('paypal-update-sub-confirmed', views.paypal_update_sub_confirmed, name="paypal-update-sub-confirmed"),
    path('django-update-sub-confirmed/<subID>', views.django_update_sub_confirmed, name="django-update-sub-confirmed"),
    
    # account management (delete account)
    path('delete-client-account', views.delete_account, name="delete-client-account"),
    
    
]
