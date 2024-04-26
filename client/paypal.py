
import requests
import json

from . models import Subscription
from django.conf import settings

# need to create a function to payal to get an authentication token

def get_access_token():
  
  data = {'grant_type': 'client_credentials'}
  
  headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en_us'
  }
  client_id = settings.SS_CLIENT_ID
  secret_id = settings.SS_SECRET_ID
  
  # make an endpoint 
  url = 'https://api.sandbox.paypal.com/v1/oauth2/token'
  
  r = requests.post(
      url, 
      auth=(client_id, secret_id), 
      headers=headers,
      data=data
    ).json()

    # extract access token
  access_token = r["access_token"]
  
  return access_token

def cancel_subscription_paypal(access_token, subID):
  
  # need to create a BEARER token
  bearer_token = 'Bearer ' + access_token
  headers = {
    'Content-Type': 'application/json',
    'Authorization': bearer_token,
  }
  
  url = 'https://api.sandbox.paypal.com/v1/billing/subscriptions/' + subID + '/cancel'
  r = requests.post(url, headers=headers)
  print(r.status_code)
  
  
# UDPATE SUBSCRIPTION:
def update_subscription_paypal(access_token, subID):
  bearer_token = 'Bearer ' + access_token
  headers = {
    'Content-Type': 'application/json',
    'Authorization': bearer_token,
  }
  
  subDetails = Subscription.objects.get(paypal_subscription_id=subID)
  current_sub_plan = subDetails.subscription_plan
  
  if current_sub_plan == 'Standard':
    new_sub_plan_id = 'P-21W29611XT561853KMYQP4OI' # to Premium
    
  elif current_sub_plan == 'Premium':
    new_sub_plan_id = 'P-8A507406TD275491SMYQP3NY' # to Standard
  
  url = 'https://api.sandbox.paypal.com/v1/billing/subscriptions/' + subID + '/revise'
  
  print(new_sub_plan_id)
  
  revision_data = {
    "plan_id": new_sub_plan_id
  }
  
  # r for request
  r = requests.post(url, headers=headers, data=json.dumps(revision_data))
  response_data = r.json()
  
  print(response_data)
  
  # HATEOAS Link
  approve_link = None
  for link in response_data.get('links', []):
    
    if link.get('rel') == 'approve':
      approve_link = link['href']
      print(approve_link)
      
  if r.status_code == 200:
    print("Request was a success")
    return approve_link
  
  else:
    print("Sorry, an error occured!")
  
  
# get current subscription

def get_current_subscription(access_token, subID):
  bearer_token = 'Bearer ' + access_token
  headers = {
    'Content-Type': 'application/json',
    'Authorization': bearer_token,
  }
  
  url = f'https://api.sandbox.paypal.com/v1/billing/subscriptions/{subID}'
  
  r = requests.get(url, headers=headers)
  
  if r.status_code == 200:
    subscription_data = r.json()
    # grab the plan_id from paypal
    current_plan_id = subscription_data.get('plan_id') 
    return current_plan_id
  else:
    print("Failed to retrieve subscription details")
    return None






