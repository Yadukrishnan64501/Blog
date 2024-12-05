from django.urls import path
from.views import (userbase,add_blog,blog_list,edit_blog,edit_profile,
edit_blog,delete_blog,my_blogs,reset_password,view_blog,view_profile,signout,add_profile,add_comment,edit_comment,delete_comment)
app_name='userpanel'
urlpatterns=[
    path('',userbase,name='userbase'),
    path('add_blog/',add_blog,name='add_blog'),
    path('edit_blog/<int:blog_id>',edit_blog,name='edit_blog'),
    path('delete_blog/<int:blog_id>',delete_blog,name='delete_blog'),
    path('edit_profile/',edit_profile,name='edit_profile'),
    path('my_blogs/', my_blogs, name='my_blogs'),
    path('blog_list/', blog_list, name='blog_list'),
    path('reset_password/',reset_password,name='reset_password'),
    path('signout/',signout,name='signout'),
    path('view_blog/<int:blog_id>',view_blog,name='view_blog'),
    path('view_profile/', view_profile, name='view_profile'),
    path('add_profile/',add_profile,name='add_profile'),
    path('add_comment/<int:blog_id>/', add_comment, name='add_comment'),
    path('edit_comment/<int:comment_id>/', edit_comment, name='edit_comment'),
    path('delete_comment/<int:comment_id>/', delete_comment, name='delete_comment'),
    

]