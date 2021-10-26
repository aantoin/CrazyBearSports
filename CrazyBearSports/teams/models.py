"""Teams Models"""
from django.db import models
from django.conf import settings
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class TeamGroup(models.Model):
    """Model for team groups such as leagues and schools."""
    group_types = ['league', 'school']
    GroupTypes = tuple(enumerate(group_types, start=1))

    name = models.CharField(max_length=30)
    short_name = models.CharField(max_length=10)
    slug = models.SlugField(max_length=30)
    group_type = models.IntegerField(choices=GroupTypes)

    page_content = RichTextUploadingField(default="",blank=True)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """Create URL for Team"""
        return reverse('team_group', args=[TeamGroup.get_group_type_string(self.group_type),str(self.slug)])
    
    @staticmethod
    def get_group_type_number(group_str):
        """Takes a string and returns the number used to filter on group_type"""
        ret = 1
        for temp_group_type in TeamGroup.GroupTypes:
            if group_str.lower() == temp_group_type[1].lower():
                return ret
            ret = ret + 1
        return 0
    @staticmethod
    def get_group_type_string(group_int):
        """Takes an integer and returns the group type string associated with it"""
        for key,value in TeamGroup.GroupTypes:
            if key == group_int:
                return value
        return None
    def group_type_string(self):
        """Instance based get_group_type_string"""
        return TeamGroup.get_group_type_string(self.group_type)


class Team(models.Model):
    """Model for teams"""
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    group = models.ForeignKey(TeamGroup,models.SET_NULL,blank=False,null=True)
    admins = models.ManyToManyField(settings.AUTH_USER_MODEL)
    page_content = RichTextUploadingField(default="",blank=True)
    card_photo = models.ImageField(upload_to='team_card_photos', blank=True, null=True)

    def __str__(self):
        return self.group.name + " - " + self.name
    def get_absolute_url(self):
        """Create URL for Team"""
        team_group = self.group
        return reverse('team', args=[TeamGroup.get_group_type_string(team_group.group_type),str(team_group.slug),str(self.slug)])

class Player(models.Model):
    """Model for players"""
    TEST = 'TS'
    POSITION_CHOICES = [
        (TEST, 'Test'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
        default=TEST,
    )
    slug = models.SlugField(max_length=50)
    team = models.ForeignKey(Team,models.SET_NULL,blank=False,null=True)

class TeamSocialMedia(models.Model):
    """Model for team social media links"""
    team = models.ForeignKey(Team,models.CASCADE,blank=False,null=False,related_name = 'social_media_links')
    link = models.URLField()
    
class TeamGroupSocialMedia(models.Model):
    """Model for team group social media links"""
    team_group = models.ForeignKey(TeamGroup,models.CASCADE,blank=False,null=False,related_name = 'social_media_links')
    link = models.URLField()
    
class TeamTicker(models.Model):
    team = models.ForeignKey(Team,models.CASCADE,blank=False,null=False, related_name = 'tickers')
    content = models.CharField(max_length=300)
    
class TeamGroupTicker(models.Model):
    team_group = models.ForeignKey(TeamGroup,models.CASCADE,blank=False,null=False, related_name = 'tickers')
    content = models.CharField(max_length=300)
    


