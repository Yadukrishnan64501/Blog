from userpanel.models import  Blog,ProfileUser,Comment, ActivityLog 

from django.contrib.auth.decorators import user_passes_test 

from django.shortcuts import render, redirect, get_object_or_404 

from django.contrib.auth import authenticate, login 

 

# Create your views here. 

# Ensure the user is an admin 

@user_passes_test(lambda u: u.is_superuser)  # Ensure only admins can access 

def admin_login(request): 

    if request.method == 'POST': 

        username = request.POST.get('username') 

        password = request.POST.get('password') 

        user = authenticate(request, username=username, password=password) 

        if user is not None: 

            login(request, user) 

            return redirect('adminpanel:home')  # Redirect to the admin home page 

        else: 

            error_message = "Invalid username or password." 

    else: 

        error_message = None 

 

    return render(request, 'adminpanel/admin_login.html', {'error_message': error_message}) 

def admin_required(function): 

    return user_passes_test(lambda u: u.is_superuser)(function) 

 

 

def home(request): 

    activities = ActivityLog.objects.all().order_by('-timestamp')   

    return render(request, 'adminpanel/admin_home.html', {'activities': activities}) 

 

@admin_required 

def user_list(request): 

    users = ProfileUser.objects.all() 

    return render(request, 'adminpanel/user_list.html', {'users': users}) 

@admin_required 

def activate_user(request, user_id): 

    user = get_object_or_404(ProfileUser, id=user_id) 

    user.is_active = True 

    user.save() 

     

    # Log the activity 

    ActivityLog.objects.create(user=request.user, action=f"Activated user {user.username}") 

     

    return redirect('adminpanel:user_list') 

 

 

@admin_required 

def deactivate_user(request, user_id): 

    user = get_object_or_404(ProfileUser, id=user_id) 

    user.is_active = False 

    user.save() 

    ActivityLog.objects.create(user=request.user, action=f"Activated user {user.username}") 

     

    return redirect('adminpanel:user_list') 

   

 

@admin_required 

def user_view(request, user_id): 

    # Retrieve the user's profile 

    user = get_object_or_404(ProfileUser, id=user_id) 

    blogs = Blog.objects.filter(user=user.user)  # user.user is the associated Django User 

    comments = Comment.objects.filter(user=user.user)   

 

     

    return render(request, 'adminpanel/user_view.html', { 

        'user': user, 

        'blogs': blogs, 

        'comments': comments, 

    }) 

 

@admin_required 

def blog_list(request): 

    blogs = Blog.objects.all() 

    return render(request, 'adminpanel/blog_list.html', {'blogs': blogs}) 

@admin_required 

def toggle_blog_visibility(request, blog_id): 

    blog = get_object_or_404(Blog, id=blog_id) 

    blog.is_visible = not blog.is_visible 

    blog.save() 

    return redirect('adminpanel:blog_list') 

@admin_required 

def blog_view(request): 

    blogs = Blog.objects.all()  # Fetch all blog posts 

    return render(request, 'adminpanel/blog_view.html', {'blogs': blogs}) 

 

@admin_required 

def comment_list(request): 

    comments = Comment.objects.all() 

    return render(request, 'adminpanel/comment_list.html', {'comments': comments}) 

@admin_required 

def toggle_comment_visibility(request, comment_id): 

    comment = get_object_or_404(Comment, id=comment_id) 

    comment.is_visible = not comment.is_visible 

    comment.save() 

        

    action = "Made blog visible" if blog.is_visible else "Made blog hidden" 

    ActivityLog.objects.create(user=request.user, action=f"{action}: {blog.title}") 

from django.contrib.auth import update_session_auth_hash 

from django.contrib.auth.forms import PasswordChangeForm 

 

@admin_required 

def reset_password(request): 

    if request.method == 'POST': 

        form = PasswordChangeForm(request.user, request.POST) 

        if form.is_valid(): 

            user = form.save() 

            update_session_auth_hash(request, user)   

            return redirect('adminpanel:home')  # Redirect to home or a success page 

    else: 

        form = PasswordChangeForm(request.user) 

     

    return render(request, 'adminpanel/reset_password.html', {'form': form}) 

 
