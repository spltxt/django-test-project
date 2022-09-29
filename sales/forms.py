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
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Дата начала')
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Дата окончания')
    chart_type = forms.ChoiceField(choices=CHART_CHOICES, label='Тип диаграммы')
    results_by = forms.ChoiceField(choices=RESULT_CHOICES, label='Сортировать по')
