from typing import List

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from matplotlib.pyplot import get
from .models import Sale, Position
from .forms import SalesSearchForm, PositionFormSet
from reports.forms import ReportForm
import pandas as pd
from .utils import get_customer_from_id, get_salesman_from_id, get_chart

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView


@login_required
def home_view(request):
    """
    Вью статистики
    """
    sales_df = None
    positions_df = None
    merged_df = None
    df = None
    chart = None
    search_form = SalesSearchForm(request.POST or None)
    report_form = ReportForm()
    no_data = None

    if request.method == "POST":
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        results_by = request.POST.get('results_by')

        sale_qs = Sale.objects.filter(created__date__lte=date_to, created__date__gte=date_from)
        if len(sale_qs) > 0:
            sales_df = pd.DataFrame(sale_qs.values())
            sales_df['customer_id'] = sales_df['customer_id'].apply(get_salesman_from_id)
            sales_df['created'] = sales_df['created'].apply(lambda x: x.strftime('%Y-%m-%d'))
            sales_df['updated'] = sales_df['updated'].apply(lambda x: x.strftime('%Y-%m-%d'))
            sales_df.rename({
                'customer_id': 'Покупатель',
                'id': 'Заказ',
                'transaction_id': 'Номер заказа',
                'total_price': 'Общая стоимость заказа',
                'created': 'Создан',
                'updated': 'Обновлён',
                'status': 'Статус заказа'
            }, axis=1, inplace=True)
            positions_data = []

            for sale in sale_qs:
                for pos in sale.get_positions():
                    obj = {
                        'position_id': pos.id,
                        'product': pos.product.name,
                        'quantity': pos.quantity,
                        'price': pos.price,
                        'sales_id': pos.get_sales_id()
                    }
                    positions_data.append(obj)

            positions_df = pd.DataFrame(positions_data)
            # merged_df = pd.merge(sales_df, positions_df, on='sales_id')

            # df = merged_df.groupby('transaction_id', as_index=False)['price'].agg('sum')

            chart = get_chart(chart_type, sales_df, results_by)
            sales_df = sales_df.to_html()
            positions_df = positions_df.to_html()
            # merged_df = merged_df.to_html()
            # df = df.to_html()

        else:
            no_data = 'В выбранном промежутке данных нет'

    context = {
        'search_form': search_form,
        'report_form': report_form,
        'sales_df': sales_df,
        'positions_df': positions_df,
        # 'merged_df': merged_df,
        # 'df': df,
        'chart': chart,
        'no_data': no_data,
    }
    return render(request, 'sales/home.html', context)


class SaleListView(LoginRequiredMixin, ListView):
    """
    Вью списка заказов текущего пользователя
    """
    model = Sale
    template_name = 'sales/main.html'
    context_object_name = 'sales'

    def get_queryset(self):
        return Sale.objects.filter(customer=self.request.user.profile)


class SaleDetailView(LoginRequiredMixin, DetailView):
    """
    Детальный вью заказа
    TODO: убрать возможность пользователям просматривать чужие заказы
    """
    model = Sale
    template_name = 'sales/detail.html'


class CreatePositionView(LoginRequiredMixin, CreateView):
    """
    Вью оформления заказа
    """
    model = Position
    fields = ['product', 'quantity']
    success_url = 'sales/'
    template_name = 'sales/test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = PositionFormSet(queryset=Position.objects.none())
        return context

    def post(self, request, *args, **kwargs):
        formset = PositionFormSet(request.POST)
        if formset.is_valid():
            return self.form_valid(formset)

    def form_valid(self, formset):
        instances = formset.save(commit=False)
        to_be_created = []

        for instance in instances:
            instance.save()
            to_be_created.append(instance.id)
        sale = Sale.objects.create(customer=self.request.user.profile)
        for position in to_be_created:
            sale.positions.add(position)
        return HttpResponseRedirect('/sales/sales-list/create-position/')

