from django.conf import settings
from django.db import models
from django.utils import timezone

# Post is our model name
class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # foreign key will link to another model
    title = models.CharField(max_length = 200)                                      # charfield is for fixed no. of characters
    text = models.TextField()                                                       # long text with no limit
    created_date = models.DateTimeField(default = timezone.now)                     # add date and time
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
    
    def __str__(self):          # return string with the post title
        return self.title