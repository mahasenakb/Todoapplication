from django.db import models

# Create your models here.
class Todo(models.Model):
    uid= models.IntegerField(primary_key = True)
    todo= models.CharField(max_length = 255)
    date= models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"todo was {self.todo}"