from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Employees, Tasks
# Register your models here.

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "contact", "gender", "department", "position", "dor"]

class TasksAdmin(admin.ModelAdmin):
    list_display = ["employee", "title", "description", "status", "start_date", "due_date"]

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type',)}),
    )


admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Tasks, TasksAdmin)

admin.site.register(CustomUser, CustomUserAdmin)
