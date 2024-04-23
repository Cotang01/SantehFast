from django.shortcuts import render
from .models import GalleryImage, Employee


def show_work_gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'work_gallery.html', {'images': images})


def show_employees_gallery(request):
    employee = Employee.objects.all()
    return render(request, 'employee_gallery.html', {'employee': employee})


