from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
      path('', views.home, name=""),
      path('register', views.register, name="register"),
      path('my-login', views.my_login, name="my-login"),
      path('user-logout', views.user_logout, name="user-logout"),
      
      # -------------- PASSWORD MANAGEMENT -------------------------
      
      #1 - ALLOW US TO ENTER OUR EMAIL IN ORDER TO RECEIVE A PASSWORD RESET LINK:
      path('reset_password', auth_views.PasswordResetView.as_view(template_name="account/password-reset.html"), name='reset_password'),
      
      # 2 - Show message stating that an email was sent to reset our password:
      path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="account/password-reset-sent.html"), name='password_reset_done'),
      
      # 3 - SEND LINK to email in order to reset password:
      path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="account/password-reset-form.html"), name='password_reset_confirm'),
      
      # 4 - If successful reset show success message showing password was changed
      path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name="account/password-reset-complete.html"), name='password_reset_complete'),
      
      
      #------------------- EMAIL VERIFICATION ----------------------
      path('email-verification/<str:uidb64>/<str:token>/', views.email_verification, name="email-verification"),
      path('email-verification-sent', views.email_verification_sent, name="email-verification-sent"),
      path('email-verification-success', views.email_verification_success, name="email-verification-success"),
      path('email-verification-failed', views.email_verification_failed, name="email-verification-failed"),
    
]
