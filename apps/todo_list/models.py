from django.db import models

# Create your models here.


class Priority(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Estate(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=60, default='Not name')
    description = models.CharField(max_length=200)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# class Tarea(models.Model):
#     description = models.CharField(max_length=200)
#     priority = models.CharField(max_length=8,
#                                  choices=("NORMAL", "ALTA", "URGENTE"),
#                                  default="NORMAL")
#     estate = models.BooleanField()
