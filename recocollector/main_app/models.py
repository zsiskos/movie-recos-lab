from django.db import models

# Create your models here.
class Reco(models.Model):
    title = models.CharField(max_length=100)
    how_heard = models.CharField(max_length=100)
    where = models.CharField(max_length=100)
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.title

class Notes(models.Model):
    date = models.DateField('watch date')
    opinion = models.TextField(max_length=500)
    reco = models.ForeignKey(Reco, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Shared opinion on {self.date}"
