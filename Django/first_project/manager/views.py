from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DetailView, DeleteView

from manager.models import Person, Worker, Manager
from manager.forms import PersonForm

# Create your views here.
#get_object_404(Person, id=20)

class GeneralList(ListView):
    def __init__(self, model, title):
        self.title = title
        self.model = model
        self.template_name = "general_list.html"

class GeneralView:
    def __init__(self, model, title):
        self.List = ListView()
        self.Edit = UpdateView()
        self.Add = CreateView()
        self.Delete = DeleteView()
        self.Detail = DetailView()
        self.model = model
        self.template_name = template_name

PersonList = GeneralList(Person, "Person")

class PersonListView(TemplateView):
    template_name = "person_list.html"

    def get(self, request, *args, **kwargs):
        context = super(PersonListView, self).get_context_data(**kwargs)

        persons = Person.objects.all()
        context ['persons'] = persons

        return render(self.request, self.template_name, context)

def person_list2(request):
    """書籍の一覧"""
    persons2 = Person.objects.all().order_by('id')
    return render(request,
                  'person_list2.html',     # 使用するテンプレート
                  {'persons2': persons2})         # テンプレートに渡すデータ

def person_edit(request, person_id=None):
    """Personの編集"""
    if person_id:
        person = get_object_or_404(Person, pk=person_id)
    else:
        person = Person()
    
    if request.method == 'POST':
        #POSTされたrequestからフォームを作成
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('person_list2')
    else:
        #personインスタンスからフォームを作成
        form = PersonForm(instance=person)
    
    return render(request, 'person_edit.html', dict(form=form, person_id=person_id))


def person_delete(request, person_id):
    """Personの削除"""
    #return HttpResponse("Person削除")
    person = get_object_or_404(Person, pk=person_id)
    person.delete()
    return redirect('person_list2')

class ManagerListView(ListView):
    model = Manager
    template = "manager_list.html"