from django.db import models

# Create your models here.

status = (
    ('todo','todo'),
    ('finished','finished'),
    ('inprogress','inprogress'),
)


class ToDo(models.Model):
    title = models.CharField(max_length=100)
    notes = models.TextField(max_length=300)
    done = models.BooleanField(default=False)
    status = models.CharField(choices=status, default='todo', max_length=130)


    def __str__(self):
        return self.title
