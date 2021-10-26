"""Admin for Stats app"""
from django.contrib import admin
from .models import (
    Game,
    DefenseStat,
    QuarterbackStat,
    RunningBackStat,
    WideReceiverStat,
    TightEndStat,
    KickerStat,
    KickOffStat,
    KickReturnStat, 
)

# Register your models here.
admin.site.register(Game)
admin.site.register(DefenseStat)
admin.site.register(QuarterbackStat)
admin.site.register(RunningBackStat)
admin.site.register(WideReceiverStat)
admin.site.register(TightEndStat)
admin.site.register(KickerStat)
admin.site.register(KickOffStat)
admin.site.register(KickReturnStat)
