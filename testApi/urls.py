
from django.contrib import admin
from django.urls import path
from myapp.views import index, taskList, taskDetail, taskCreate, taskUpdate, taskDelete


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', index),
    path('task-list/', taskList),
    path('task-detail/<str:pk>/', taskDetail),
    path('task-create/', taskCreate),
    path('task-update/<str:pk>/', taskUpdate),
    path('task-delete/<str:pk>/', taskDelete)
]
