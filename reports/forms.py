from django import forms
from .models import Report


class ReportForm(forms.ModelForm):
    """
    Форма создания отчёта
    """
    class Meta:
        model = Report
        fields = ('name', 'remarks')
