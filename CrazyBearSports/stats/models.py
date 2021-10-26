"""Models for stats"""
from django.db import models
from teams.models import Team,Player

# Create your models here.
class Game(models.Model):
    """Model for a game for stat recording."""
    group_types = ['league', 'school']
    GroupTypes = tuple(enumerate(group_types, start=1))

    name = models.CharField(max_length=30)
    team1 = models.ForeignKey(Team,models.SET_NULL,blank=False,null=True,related_name='games_team1')
    team2 = models.ForeignKey(Team,models.SET_NULL,blank=False,null=True,related_name='games_team2')
    date = models.DateField(blank=False,null=False)

    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     """Create URL for Team"""
    #     return reverse('team_group', args=[TeamGroup.get_group_type_string(self.group_type),str(self.slug)])
    

class Stat(models.Model):
    """Parent class for a stat group"""
    first_name = models.CharField(max_length=50,default='')
    last_name = models.CharField(max_length=50,default='')


    class Meta:
        abstract = True

class DefenseStat(Stat):
    """Defense Stat"""
    tackles = models.IntegerField(blank=True,null=True,default=0)
    tackles_for_loss = models.IntegerField(blank=True,null=True,default=0)
    pass_break_ups = models.IntegerField(blank=True,null=True,default=0)
    interceptions = models.IntegerField(blank=True,null=True,default=0)
    force_fumbles = models.IntegerField(blank=True,null=True,default=0)
    fumble_recovery = models.IntegerField(blank=True,null=True,default=0)
    sacks = models.IntegerField(blank=True,null=True,default=0)
    qb_hurries = models.IntegerField(blank=True,null=True,default=0)
    touchdowns = models.IntegerField(blank=True,null=True,default=0)
    fumble_return_yardage = models.IntegerField(blank=True,null=True,default=0)
    interception_return_yardage = models.IntegerField(blank=True,null=True,default=0)


class QuarterbackStat(Stat):
    """Quarterback Stat"""
    pass_attempts = models.IntegerField(blank=True,null=True,default=0)
    pass_completions = models.IntegerField(blank=True,null=True,default=0)
    pass_yardage = models.IntegerField(blank=True,null=True,default=0)
    touchdowns = models.IntegerField(blank=True,null=True,default=0)
    two_point_conversions = models.IntegerField(blank=True,null=True,default=0)
    interceptions = models.IntegerField(blank=True,null=True,default=0)
    fumbles_loss = models.IntegerField(blank=True,null=True,default=0)
    rushing_attempts = models.IntegerField(blank=True,null=True,default=0)
    rush_yardage = models.IntegerField(blank=True,null=True,default=0)


class RunningBackStat(Stat):
    """Running Back Stat"""
    rushing_attempts = models.IntegerField(blank=True,null=True,default=0)
    rushing_yardage = models.IntegerField(blank=True,null=True,default=0)
    receptions = models.IntegerField(blank=True,null=True,default=0)
    reception_yardage = models.IntegerField(blank=True,null=True,default=0)
    touchdowns = models.IntegerField(blank=True,null=True,default=0)
    two_point_conversions = models.IntegerField(blank=True,null=True,default=0)
    fumbles_loss = models.IntegerField(blank=True,null=True,default=0)

    
class WideReceiverStat(Stat):
    """Wide Receiver Stat"""
    rushing_attempts = models.IntegerField(blank=True,null=True,default=0)
    rushing_yardage = models.IntegerField(blank=True,null=True,default=0)
    receptions = models.IntegerField(blank=True,null=True,default=0)
    reception_yardage = models.IntegerField(blank=True,null=True,default=0)
    touchdowns = models.IntegerField(blank=True,null=True,default=0)
    two_point_conversions = models.IntegerField(blank=True,null=True,default=0)
    fumbles_loss = models.IntegerField(blank=True,null=True,default=0)

    
class TightEndStat(Stat):
    """Tight End Stat"""
    receptions = models.IntegerField(blank=True,null=True,default=0)
    reception_yardage = models.IntegerField(blank=True,null=True,default=0)
    touchdowns = models.IntegerField(blank=True,null=True,default=0)
    two_point_conversions = models.IntegerField(blank=True,null=True,default=0)
    fumbles_loss = models.IntegerField(blank=True,null=True,default=0)

    
class KickerStat(Stat):
    """Kicker Stat"""
    extra_points = models.IntegerField(blank=True,null=True,default=0)
    field_goal_attempts = models.IntegerField(blank=True,null=True,default=0)
    field_goals = models.IntegerField(blank=True,null=True,default=0)
    two_points = models.IntegerField(blank=True,null=True,default=0)
    tackles = models.IntegerField(blank=True,null=True,default=0)

    
class KickOffStat(Stat):
    """Kick Off Stat"""
    tackles = models.IntegerField(blank=True,null=True,default=0)
    forced_fumbles = models.IntegerField(blank=True,null=True,default=0)
    fumble_recovery = models.IntegerField(blank=True,null=True,default=0)
    touchdowns = models.IntegerField(blank=True,null=True,default=0)

    
class KickReturnStat(Stat):
    """Kick Return Stat"""
    return_attempts = models.IntegerField(blank=True,null=True,default=0)
    return_yardage = models.IntegerField(blank=True,null=True,default=0)
    fumbles = models.IntegerField(blank=True,null=True,default=0)
    touchdowns = models.IntegerField(blank=True,null=True,default=0)

    
