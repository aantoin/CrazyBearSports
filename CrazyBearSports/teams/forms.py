"""Forms for team app"""
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from teams.models import Team

class TeamEditForm(forms.ModelForm):
    """Form for editing team page content"""
    page_content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Team
        fields = ['page_content']