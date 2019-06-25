from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView, TemplateResponseMixin, ContextMixin
from django.views.generic import View, DetailView
from django.http import HttpResponse
from django.utils.decorators import method_decorator

class BookDetail(DetailView):
    model = Book


class DashboardTemplateView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardTemplateView, self).get_context_data(*args, **kwargs)
        context["title"] = "DasshBoard"
        return context


class MyView(ContextMixin, TemplateResponseMixin, View):
    template_name = "myview.html"

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['title'] = "Myview"
        return self.render_to_response(context)
