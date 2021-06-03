from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.
class Blog_Website(models.Model):
    Author = models.CharField(max_length = 200)
    Title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 200)
    Description = models.TextField()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.Title)
        super(Blog_Website,self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('hello', kwargs = {'slug':self.slug})