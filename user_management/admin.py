from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from user_management.models import TodoUserProfile


class TodoUserProfileInline(admin.StackedInline):

    model = TodoUserProfile


class TodoUserAdmin(UserAdmin):

    inlines = (TodoUserProfileInline, )


admin.site.unregister(User)
admin.site.register(User, TodoUserAdmin)
