from django.shortcuts import render
from profiles.models import Profile
from django.http import JsonResponse
from .utils import get_report_image, is_ajax
from .models import Report
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class ReportListView(LoginRequiredMixin, ListView):
    """
    Вью списка отчётов
    """
    model = Report
    template_name = 'reports/main.html'


class ReportDetailView(LoginRequiredMixin, DetailView):
    """
    Детальный вью отчёта
    """
    model = Report
    template_name = 'reports/detail.html'


@login_required
def create_report_view(request):
    """
    Вью создания отчёта
    """
    if is_ajax(request):
        name = request.POST.get('name')
        remarks = request.POST.get('remarks')
        image = request.POST.get('image')

        img = get_report_image(image)

        author = Profile.objects.get(user=request.user)
        Report.objects.create(name=name, remarks=remarks, image=img, author=author)
        return JsonResponse({'msg': 'send'})
    return JsonResponse({})
