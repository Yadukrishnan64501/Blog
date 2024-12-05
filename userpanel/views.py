from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog,ProfileUser,Comment
from.forms import blogform,userform,CommentForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash



# Create your views here.
@login_required
def userbase(request):
    blogs = Blog.objects.prefetch_related('userpanel_comments').all()
    return render(request, 'userpanel/user_home.html', {'blogs': blogs})
  
@login_required
def add_blog(request):
    
    
    
    if request.method =='POST':
        form =blogform(request.POST,request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)  # Don't save it yet
            blog.user = request.user       # Set the user
            blog.save()                    # Now save it
            messages.success(request, 'NEW BLOG ADDED')
            return redirect('userpanel:my_blogs')
       
    else:
        form =blogform()
    context ={
        'form':form
     }
    return render(request,'userpanel/add_blog.html',context)
@login_required
def my_blogs(request):
    blogs = Blog.objects.filter(user=request.user).order_by('-id')  # Filter by user
    return render(request, 'userpanel/my_blogs.html', {'blogs': blogs})
 
   
@login_required
def edit_blog(request,blog_id):
    blog= get_object_or_404(Blog, id=blog_id)
    if request.method =='POST':
        form =blogform(request.POST,request.FILES)
        if form.is_valid():
         form.save()
        messages.success(request,' BLOG UPDATED')
        return redirect('sitevisitor:sitebase')
    else:
        form =blogform()
    context ={
        'form':form
     }
    return render(request,'userpanel/edit_blog.html',context)
@login_required
def delete_blog(request,blog_id):
    blog=get_object_or_404(Blog,id=blog_id)
    blog.delete()
    messages.success(request,'BLOG DELETED SUCCESSFULLY')
    return redirect('userpanel:my_blogs')
@login_required
def signout(request):
    logout(request)
    return redirect('sitevisitor:user_login')

@login_required
def add_comment(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.user = request.user
            comment.save()
            messages.success(request, 'Comment added!')
            return redirect('userpanel:blog_list', blog_id=blog.id)
    else:
        form = CommentForm()

    return render(request, 'userpanel/add_comment.html', {'form': form, 'blog': blog})

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.user:
        messages.error(request, 'You are not allowed to edit this comment.')
        return redirect('userpanel:blog_list', blog_id=comment.blog.id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment updated!')
            return redirect('userpanel:blog_list', blog_id=comment.blog.id)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'userpanel/edit_comment.html', {'form': form, 'comment': comment})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.user:
        comment.delete()
        messages.success(request, 'Comment deleted successfully!')
    else:
        messages.error(request, 'You are not allowed to delete this comment.')

    return redirect('userpanel:blog_list', blog_id=comment.blog.id)




    
  
@login_required  
def edit_profile(request):
    return render(request,'userpanel/edit_profile.html')
@login_required
def blog_list(request):
    blogs = Blog.objects.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            
            blog_id = request.POST.get('blog_id')
            blog = get_object_or_404(Blog, id=blog_id)
            comment = comment_form.save(commit=False)
            comment.blog = blog
            comment.user = request.user
            comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect('userpanel:blog_list')  # Redirect after POST
    else:
        comment_form = CommentForm()

    return render(request, 'userpanel/blog_list.html', {
        'blogs': blogs,
        'comment_form': comment_form,
    })
    
   

def reset_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password was successfully updated!')
            return redirect('userpanel:userbase')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'userpanel/reset_password.html', {'form': form})
@login_required
def view_blog(request):
    return render(request,'userpanel/view_blog.html')
@login_required
def add_profile(request):
    if request.method =='POST':
        form =userform(request.POST,request.FILES)
        if form.is_valid():
         form.save()
        messages.success(request,'profile ADDED')
        return redirect('userpanel:my_blogs')
    else:
        form =userform()
    context ={
        'form':form
     }
    return render(request,'userpanel/add_profile.html',context)
    
@login_required   
def view_profile(request):
      
    profile = get_object_or_404(ProfileUser, user=request.user)
    return render(request, 'userpanel/view_profile.html', {'profile': profile})

    
 


