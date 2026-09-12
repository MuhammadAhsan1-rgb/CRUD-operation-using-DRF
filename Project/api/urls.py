from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.get_data),
    path('create-department/' , views.post_department),
    path('create-employee/' , views.post_employee),
    path('update-department/<int:pk>' , views.put_patch_data_department),
    path('update-employee/<int:pk>' , views.put_patch_data_employee),
    path('delete-department/<int:pk>' , views.delete_department),
    path('delete-employee/<int:pk>' , views.delete_employee),
]
