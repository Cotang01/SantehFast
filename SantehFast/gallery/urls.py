from django.urls import path
from .views import show_work_gallery, show_employees_gallery

urlpatterns = [
    path('works', show_work_gallery, name='work_gallery'),
    path('employee', show_employees_gallery, name='employee_gallery')
]
