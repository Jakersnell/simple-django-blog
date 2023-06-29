from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

# these models act as an interface for SQL interaction

class Profile(models.Model):
    # defines boundaries and constraints on Profile oject
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(default=' ', max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} profile'

    # saves object and then resizes saved image in path
    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


# one to many relationship with .ForeignKey user model
# defines constraints for SQL interaction
class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_photos')
    date_posted = models.DateTimeField(auto_now_add=True)
