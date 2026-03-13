from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=225)

    class Meta:
        ordering = ('title')
        verbose_name_plural = 'Categories'

def _srt_(self):
            return self.title

            class Post(models.Model):

                ACTIVATE = 'activate'
                DRAF = 'draft'

                CHOICES_STATUS = {
                    (ACTIVE,'Active')
                    (DRAFT,'Draft')
                }

category = models.ForeingKey(Category,related_name='posts', on_delete=models.CASCADE)
title = models.CharField(max_length=225)
intro = models.TextField()
body = models.TextField()
created_at = models.DateTimeField(auto_now_add=True)
status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
image = models.ImageField(upload_to='unpload', blank=True, null=True)

def _str_(self):
    return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name