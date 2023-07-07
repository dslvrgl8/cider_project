from django.db import models

# Create your models here.
class Cider(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    verified_cider = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

# below Artist Model

class Flavor(models.Model):

    title = models.CharField(max_length=150)
    rating = models.IntegerField(default=0)
    cider = models.ForeignKey(Cider, on_delete=models.CASCADE, related_name="flavors")

    def __str__(self):
        return self.title
    
class Favorite(models.Model):

    title = models.CharField(max_length=150)
    # this is going to create the many to many relationship and join table
    flavors = models.ManyToManyField(Flavor)

    def __str__(self):
        return self.title

