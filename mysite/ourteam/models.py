from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    password = models.CharField(max_length=8)
    email = models.EmailField(max_length=100, unique=True)
    num = models.CharField(max_length=50)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)


    def __str__(self):
        return self.user_name



class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100, default='')
    user_name = models.ForeignKey('User', on_delete=models.PROTECT)
    group = models.ForeignKey('Group', on_delete=models.PROTECT)
    project = models.ForeignKey('Project', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(blank=True)
    finished = models.BooleanField(blank=True)
    group = models.ForeignKey('Group', on_delete=models.PROTECT)

    def __str__(self):
        return self.title









