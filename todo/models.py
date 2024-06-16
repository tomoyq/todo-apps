from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 100)
    created_at = models.DateField(auto_now_add = True)
    success = models.BooleanField(default = False)

    def __str__(self):
        return self.title