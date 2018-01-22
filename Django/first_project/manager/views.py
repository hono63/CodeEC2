from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView

from manager.models import *
from manager.forms import *

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

def person_edit(request, person_id=None):
    """Personの編集"""
    #return HttpRequest("Person編集")
    if person_id:
        person = get_object_or_404(Person, pk=person_id)
    else:
        person = Person()
    
    if request.method == 'POST':
        #POSTされたrequestからフォームを作成
        form = PersonForm(request.POST, isinstance=person)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('PersonListView')
    else:
        #personインスタンスからフォームを作成
        form = PersonForm(instance=person)
    
    return render(request, 'person_edit.html', dict(form=form, person_id=person_id))


def person_delete(request, person_id):
    """Personの削除"""
    return HttpRequest("Person削除")