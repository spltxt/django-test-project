from django import forms

CHART_CHOICES = (
    ('#1', 'Столбчатая диаграмма'),
    ('#2', 'Круговая диаграмма'),
    ('#3', 'Линейная диаграмма'),
)

RESULT_CHOICES = (
    ('#1', 'Id заказа'),
    ('#2', 'Дата продажи'),
)

class SalesSearchForm(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)
    results_by = forms.ChoiceField(choices=RESULT_CHOICES)

