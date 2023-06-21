from django.urls import path
from . import views
from . import dashboardviews
from . import employeeviews

urlpatterns = [
    path('', views.Login, name='dashboard'), 
    path('logout/', views.Logout, name='logout'),

# dashboard views
    path('HR/', dashboardviews.Users, name='users'),
    path('task/', dashboardviews.Jobs, name='task'),
    path('task/<int:task_id>/', dashboardviews.edit_task, name='task'),
    path('delete-task/<int:task_id>/', dashboardviews.delete_task, name='delete_task'),


    # employee views
     path('Employee/', employeeviews.Jobs, name='Employee'),
     path('Employee/<int:task_id>/', employeeviews.edit_task, name='Employee')
]
