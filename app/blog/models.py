from django.db import models
from django.utils import timezone

# Create your models here.



class Blog(models.Model):
    class Meta():
        db_table = "blog"

    blog_title = models.CharField(max_length=200)
    blog_text = models.TextField()
    blog_date = models.DateTimeField(default=timezone.now)
    blog_author = models.ForeignKey('auth.User')
    blog_published_date = models.DateTimeField(blank=True, null=True)

    # blog_likes = models.IntegerField(default=0)
    def publish(self):
        self.blog_published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.blog_title

    #class Subscribe(models.Model):
 #   Subscribe = auth_user.objects.all().filter(id)

