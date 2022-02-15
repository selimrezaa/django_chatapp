from django.db import models

# Create your models here.


class Group(models.Model):
    group_name = models.CharField(max_length=255)

    def __str__(self):
        return self.group_name

class Chat(models.Model):
    content = models.CharField(max_length=255)
    timestap = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.content