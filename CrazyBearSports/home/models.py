"""Models for Home page"""
from django.utils import timezone
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Sponsor(models.Model):
    """Model for Sponsors"""
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='sponsor_logos', blank=True, null=True)
    url = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.name

class Ticker(models.Model):
    """Model for Ticker"""
    content = models.CharField(max_length=300)

class Update(models.Model):
    """Model for Updates"""
    content     = RichTextUploadingField(default="",blank=True)
    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs): # pylint: disable=signature-differs
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Update, self).save(*args, **kwargs)