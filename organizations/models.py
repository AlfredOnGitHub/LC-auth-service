from django.db import models
from datetime import datetime, timedelta
from django.core.validators import EmailValidator
from PIL import Image

class Organization(models.Model):
    photo = models.ImageField(upload_to='organization_photos/', blank=True, null=True)
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(validators=[EmailValidator()], null=True)
    renewal_date = datetime.now().date() + timedelta(days=365)
    workers = models.ManyToManyField('Person', related_name='trabajadores', blank=True)
    partners = models.ManyToManyField('Person', related_name='socios', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            img = Image.open(self.photo.path)
            if img.height > 400 or img.width > 200:
                output_size = (400, 200)
                img.thumbnail(output_size)
                img.save(self.photo.path)

class Person(models.Model):
    photo = models.ImageField(upload_to='person_photos/', blank=True, null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(validators=[EmailValidator()], null=True)
    renewal_date = datetime.now().date() + timedelta(days=365)
    wallet = models.FloatField(default=0.0)
    history = models.JSONField(blank=True)
    organization = models.ManyToManyField('Organization', related_name='orgs')

    def __str__(self):
        return self.name
