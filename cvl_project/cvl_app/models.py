from email import message
from email.mime import image
from email.quoprimime import quote
from msilib.schema import Media
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.

# media model

class Media(models.Model):
    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media File'
        ordering = ['name']
    
    image = models.ImageField(blank=True, null=True, upload_to='media')
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

# service learnmore
class Services_More(models.Model):
    class Meta:
        verbose_name_plural = 'Services More'
        verbose_name = 'Service More'
        ordering = ['name']

    thumbnail = models.ImageField(blank=True, null=True, upload_to='services')
    name = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=2000, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


# service model

class Services(models.Model):
    class Meta:
        verbose_name_plural = 'Services'
        verbose_name = 'Service'
        ordering = ['name']
    
    name = models.CharField(max_length=200, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='about')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

# about model

class About(models.Model):
    class Meta:
        verbose_name_plural = 'About Profiles'
        verbose_name = 'About profile'
        ordering = ['name']
    
    name = models.CharField(max_length=200, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='about')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

# contact model

class Contact(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'

    firstname = models.CharField(max_length=200,verbose_name='First Name')
    lastname = models.CharField(max_length=200,verbose_name='Last Name')
    phone = models.IntegerField(verbose_name='Phone Number')
    email = models.EmailField(verbose_name='email')
    message = models.TextField(blank=True, verbose_name='message')

    def __str__(self):
        return f'{self.firstname}' 


