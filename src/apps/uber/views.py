import json
#
from django.http import JsonResponse
from django.views.generic import TemplateView
#
from celery.result import AsyncResult
#
from src.celery import app
from src.apps.uber import tasks


def celery_results(request, task_id):
    res = AsyncResult(str(task_id), app=app)

    response = {'state': res.state }
    if res.state == 'SUCCESS':
        response.update(results=json.loads(res.get()))

    return JsonResponse(response)


def test_tasks_add(request, x, y, delay=0):
    task = tasks.add.delay(x, y, delay)
    return JsonResponse({'task_id': task.id})


def test_tasks_mul(request, x, y, delay=0):
    task = tasks.mul.delay(x, y, delay)
    return JsonResponse({'task_id': task.id})


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def chart_total_trips_per_year(self):
        task = tasks.total_trips_per_year.delay()
        return task.id
    
    def chart_percentage_trips_per_status_and_year(self):
        task = tasks.percentage_trips_per_status_and_year.delay()
        return task.id

    def get_context_data(self, **kwargs):
        ctx = super(DashboardView, self).get_context_data(**kwargs)
        ctx['total_trips_per_year'] = self.chart_total_trips_per_year()
        ctx['percentage_trips_per_status_and_year'] = self.chart_percentage_trips_per_status_and_year()
        return ctx