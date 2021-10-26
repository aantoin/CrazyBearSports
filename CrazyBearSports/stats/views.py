"""Views for Stats application"""
from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.decorators import user_passes_test
from django.forms import formset_factory
from .forms import(
    DefenseForm
)
from .models import (
    Stat,
    DefenseStat,
    QuarterbackStat,
    RunningBackStat,
    WideReceiverStat,
    TightEndStat,
    KickerStat,
    KickOffStat,
    KickReturnStat,
)

# Create your views here.
def stats(request):
    context = {}
    #for class_iter in ["DefenseStat","QuarterbackStat","RunningBackStat","WideReceiverStat","TightEndStat","KickerStat","KickOffStat","KickReturnStat ",]:
    for class_iter in [DefenseStat,QuarterbackStat,RunningBackStat,WideReceiverStat,TightEndStat,KickerStat,KickOffStat,KickReturnStat]:
        field_names = [f.name for f in class_iter._meta.get_fields(include_parents=False)[1+len(Stat._meta.get_fields())::]]
        context[class_iter.__name__ + '_field_names'] = [f.verbose_name for f in class_iter._meta.get_fields(include_parents=False)[1+len(Stat._meta.get_fields())::]]
        context[class_iter.__name__]=class_iter.objects.all().values('player__id','player__first_name','player__last_name','player__position').annotate(**{fn : Sum(fn) for fn in field_names})
        print(class_iter.__name__, context[class_iter.__name__])
    return render(request, 'stats/stats.html', context)




@user_passes_test(lambda u: u.is_superuser)
def upload(request):
    """Upload new stats from google sheets"""
    context = {}


    # Call the Sheets API
    from googleapiclient.discovery import build
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    KEY = 'AIzaSyAF81X8t6PuaIEWcIwVXyIHt7V_84wUJbA'
    SAMPLE_SPREADSHEET_ID = '1ZiEsimCB9RRMm07bsft0VqOYObQhXJW1tK_fqomuF2I'
    SAMPLE_RANGE_NAME = 'Sheet1!A2:M'
    service = build('sheets','v4',developerKey=KEY)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    context['values'] = values

    statFormset = formset_factory(DefenseForm,extra=0)
    formset = statFormset(initial=[{'first_name':'a','last_name':'b'},{'first_name':'c','last_name':'d'}])
    context['formset']=formset

    return render(request, 'stats/upload.html', context)