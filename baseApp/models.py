from django.db import models



class Tools(models.Model):
    toolName = models.CharField(max_length=200)
    toolDescription = models.CharField(max_length=500)
    classT = models.CharField(max_length=200) 
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.toolName} -- ESC tool'