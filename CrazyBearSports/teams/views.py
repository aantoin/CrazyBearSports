"""Teams Views"""
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

from .models import TeamGroup, Team
from .forms import TeamEditForm

# Create your views here.
def team_group_view(request, group_type, group):
    """Team_group (league, school) view"""
    team_group = TeamGroup.objects.filter(
        group_type=TeamGroup.get_group_type_number(group_type),
        slug=group
    ).first()
    if team_group is None:
        raise Http404("Group does not exist")
    return render(
        request, 'teams/team_group.html',
        {"team_group":team_group, "teams":Team.objects.filter(group=team_group)}
    )

def team_view(request, group_type, group, team, **kwargs):
    """Team view"""
    team_group = TeamGroup.objects.filter(
        group_type=TeamGroup.get_group_type_number(group_type),
        slug=group
    ).first()
    if team_group is None:
        raise Http404("Group does not exist")
    team = Team.objects.filter(
        group = team_group,
        slug = team,
    ).first()
    if team is None:
        raise Http404("Team does not exist")
    context = {"team_group":team_group,"team":team}
    form = None
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TeamEditForm(request.POST)
        print("1")
        # check whether it's valid:
        if form.is_valid():
            print("2")
            # process the data in form.cleaned_data as required
            team.page_content = form.cleaned_data['page_content']
            team.save()
            return HttpResponseRedirect(team.get_absolute_url())
        else:
            print("FORM NOT VALID")
            print(form.errors)
    action = kwargs.get('action')
    if action == 'edit_inline':
        if form is None:
            form = TeamEditForm(instance=team)
        context['form']=form
        return render(request, 'teams/team_edit_inline.html',context)
    if action == 'edit':
        if form is None:
            form = TeamEditForm(instance=team)
        context['form']=form
    return render(request, 'teams/team.html',context)