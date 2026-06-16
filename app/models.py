from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.
class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')
  
class Category(models.Model):
    name=models.CharField(max_length=100)
    slug = models.SlugField(blank=True)   # ✅ added slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.name
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='products/')
    description=models.TextField()
    specifications=RichTextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class ServiceCategory(models.Model):
    name=models.CharField(max_length=100)
    slug = models.SlugField(blank=True)   # ✅ added slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Service(models.Model):
    category=models.ForeignKey(ServiceCategory,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField()
    about_heading=models.CharField(max_length=200)
    about_description=models.TextField()
    key_features_heading=models.CharField(max_length=200)
    key_features_description=RichTextField(null=True, blank=True)
    image=models.ImageField(upload_to='services/')
    
    def __str__(self):
        return self.name
    

class Gallery(models.Model):
    image=models.ImageField(upload_to='gallery/')
    title=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    subject=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return self.name


class Client(models.Model):
    name=models.CharField(max_length=100)
    logo=models.ImageField(upload_to='clients/')

    def __str__(self):
        return self.name


class PolicyPage(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    author = models.CharField(max_length=100, default='Admin')
    category = models.CharField(max_length=100, blank=True)
    featured_image = models.ImageField(upload_to='blogs/')
    excerpt = models.TextField(help_text='Short summary shown on the blog listing cards.')
    content = RichTextField()
    is_published = models.BooleanField(default=True)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title