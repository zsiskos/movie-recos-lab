from django.db import models

# Create your models here.
class Reco(models.Model):
    title = models.CharField(max_length=100)
    how_heard = models.CharField(max_length=100)
    where = models.CharField(max_length=100)
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.title




# recos = [
#     Reco('Fight Club', 'Zoe', 'NetFlix', 'A mind fuck movie'),
#     Reco('Army of Darkness', 'James', 'NetFlix', 'The best B rated horror flick ever'),
#     Reco('Onward', 'John', 'Disney', 'a funny feel good Disney flick'),
#     Reco('The Outsider', 'James\'s work friend', 'Crave', 'same director as ozarks, basedo n stephen king, makes y ou think and creepy'),
#     Reco('The Servant', 'James', 'AppleTV', 'so creepy, dir. by M. Night Shamalaman'),
#     Reco('Bombshell', 'Ads', 'GooglePlay', 'true story, strong female characters'),
#     Reco('House of 1000 Corpses', 'Joe', 'Netflix', 'scary AF'),
# ]