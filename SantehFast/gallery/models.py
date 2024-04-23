from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    patronymic = models.CharField(max_length=15, blank=True, null=True)
    proficiency = models.CharField(max_length=15)
    experience = models.IntegerField(verbose_name='Опыт работы',
                                     blank=True, null=True)
    avatar = models.ImageField(upload_to='images/employee', null=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic} {self.proficiency}'

    class Meta:
        verbose_name = 'Работники'
        verbose_name_plural = 'Работники'


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='images/work')
    author = models.ForeignKey(Employee, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.image.name} {self.author} {self.upload_date}'

    class Meta:
        verbose_name = 'Галерея работ'
        verbose_name_plural = 'Галерея работ'

