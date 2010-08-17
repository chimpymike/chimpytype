from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    url = models.SlugField(max_length=200)
    publish_date = models.DateTimeField()
    author = models.ForeignKey(User, related_name="author_user")
    creation_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="created_by_user", editable=False)
    last_update_date = models.DateTimeField(auto_now=True)
    last_updated_by = models.ForeignKey(User, related_name="last_updated_by_user", editable=False)

    def __unicode__(self):
        return self.title
    
    
