# urls.py
from django.urls import path
from .views import home, user_list,user_view,admin_login, activate_user, deactivate_user, blog_list,blog_view,toggle_blog_visibility, comment_list, toggle_comment_visibility, reset_password
app_name='adminpanel'
urlpatterns = [
    path('', home, name='home'),
    path('admin_login/', admin_login, name='admin_login'),  # Custom admin login
    path('user_list/', user_list, name='user_list'),
    path('user_view/<int:user_id>/', user_view, name='user_view'),  
    path('activate_user/<int:user_id>/', activate_user, name='activate_user'),
    path('deactivate_user/<int:user_id>/', deactivate_user, name='deactivate_user'),
    path('blog_list/', blog_list, name='blog_list'),
    path('blog_view/', blog_view, name='blog_view'),
    path('toggle_blog_visibility/<int:blog_id>/', toggle_blog_visibility, name='toggle_blog_visibility'),
    path('comment_list/', comment_list, name='comment_list'),
    path('toggle_comment_visibility/<int:comment_id>/', toggle_comment_visibility, name='toggle_comment_visibility'),
    path('reset_password/', reset_password, name='reset_password'),
]
