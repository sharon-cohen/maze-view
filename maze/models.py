from django.db import models



# Create your models here.
class function(models.Model):
    dateCreated = models.DateField(auto_now_add=True)
    dateCompleted = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=70)
    description = models.TextField(default=False)
    avatar = models.ImageField(upload_to='projects/images')
    
    class Meta:
        ordering = ['-dateCreated']

    # this method is the default human-readable representation of the object. Django will use it in many places
    # such as the admin panel
    def __str__(self):
        return self.title