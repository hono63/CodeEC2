from django.shortcuts import render
from django.views.generic import TemplateView

from manager.models import *

# Create your views here.
#get_object_404(Person, id=20)

class WorkerListView(TemplateView):
    template_name = "worker_list.html"

    def get(self, request, *args, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)

        workers = Worker.objects.all()
        context ['workers'] = workers

        return render(self.request, self.template_name, context)

class PersonListView(TemplateView):
    template_name = "person_list.html"

    def get(self, request, *args, **kwargs):
        context = super(PersonListView, self).get_context_data(**kwargs)

        persons = Person.objects.all()
        context ['persons'] = persons

        return render(self.request, self.template_name, context)
