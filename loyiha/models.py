from django.db import models

# Create your models here.

class CustomUser(models.Model):
    USER = (
        (1, 'ADMIN'),
        (2, 'USTOZ'),
        (3, 'STUDENT'),
    )
    user_type = models.CharField(choices=USER, max_length=50, default=3)
    custom_name = models.CharField(max_length=50)
    custom_lastname = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='media/user_pic/')
    def __str__(self):
        return self.custom_name


class Course(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Guruh(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Tolov(models.Model):
    tolov_type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tolov_type

class Student(models.Model):
    address = models.TextField()
    rasmi = models.ImageField(upload_to='media/profile_pic/')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    telefon = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    guruh_id = models.ForeignKey(Guruh, on_delete=models.DO_NOTHING)
    tolov_id = models.ForeignKey(Tolov, on_delete=models.DO_NOTHING)
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
class Yangiliklar(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=300)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title