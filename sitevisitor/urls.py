from django.urls import path
from.views import sitebase,registration,forgot_password,user_login,otp,reset_password
app_name='sitevisitor'
urlpatterns=[
    path('',sitebase,name='sitebase'),
    path('registration/',registration,name='registration'),
    path('forgot_password/',forgot_password,name='forgot_password'),
    path('user_login/',user_login,name='user_login'),
    path('reset_password/',reset_password),
    

]