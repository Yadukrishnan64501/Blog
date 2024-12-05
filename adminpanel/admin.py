from django.contrib import admin
from userpanel.models import Blog
from userpanel.models import ProfileUser
from userpanel.models import Comment
from userpanel.models import ActivityLog

# Register your models here.

admin.site.register(Blog)
admin.site.register(ProfileUser)
admin.site.register(Comment)
admin.site.register( ActivityLog)


