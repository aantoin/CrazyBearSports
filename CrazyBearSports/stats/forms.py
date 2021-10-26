from django import forms
from .models import DefenseStat

class StatForm(forms.ModelForm):
    first_name = forms.CharField(label='First name', max_length=50)
    last_name = forms.CharField(label='Last name', max_length=50)


class DefenseForm(StatForm):
    class Meta:
        model = DefenseStat
        fields = ['first_name','last_name','tackles','tackles_for_loss','pass_break_ups',
                    'interceptions','force_fumbles','fumble_recovery',
                    'sacks','qb_hurries','touchdowns',
                    'fumble_return_yardage','interception_return_yardage',]

    def __init__(self, *args, **kwargs):
        super(DefenseForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        for field in self.fields:
                self.fields[field].disabled = True