from django.contrib import admin

from .models import TeamGroup, Team, Player, TeamSocialMedia, TeamGroupSocialMedia, TeamTicker, TeamGroupTicker

# Register your models here.
class TeamGroupSocialMediaInlineAdmin(admin.StackedInline):
    extra = 0
    model = TeamGroupSocialMedia
class TeamGroupTickerInlineAdmin(admin.StackedInline):
    extra = 0
    model = TeamGroupTicker
class TeamInline(admin.TabularInline):
    model = Team
    exclude = ['page_content']
class TeamGroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [TeamGroupSocialMediaInlineAdmin, TeamGroupTickerInlineAdmin, TeamInline,]
admin.site.register(TeamGroup, TeamGroupAdmin)

class TeamSocialMediaInlineAdmin(admin.StackedInline):
    extra = 0
    model = TeamSocialMedia
class TeamTickerInlineAdmin(admin.StackedInline):
    extra = 0
    model = TeamTicker
class TeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [TeamSocialMediaInlineAdmin, TeamTickerInlineAdmin]
admin.site.register(Team, TeamAdmin)


admin.site.register(Player)