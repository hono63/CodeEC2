from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DetailView, DeleteView
from django.forms.models import model_to_dict

from manager.models import Person, Worker, Manager
from manager.forms import PersonForm

# Create your views here.
#get_object_404(Person, id=20)

class GeneralList(ListView):
    template_name = "general_list.html"
    def setting(self, model, title):
        self.title = title
        self.model = model

class GeneralDetail(DetailView):
    template_name = "general_detail.html"
    def setting(self, model, form, title):
        self.title = title
        self.model = model
        self.form = form
    
    def get_context_data(self, **kwargs):
        """
        参考：
        https://stackoverflow.com/questions/10353804/how-do-i-loop-through-fields-of-an-object
        https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-display/
        https://stackoverflow.com/questions/2415865/iterating-through-two-lists-in-django-templates
        """
        context = super().get_context_data(**kwargs)

        #dicobj = self.form(data=model_to_dict(self.model.objects.get(pk=kwargs["pk"])))
        #fields = self.form(data=model_to_dict(kwargs["object"]))
        fields = kwargs["object"].__dict__
        context ['fields'] = zip(fields.keys(), fields.values())

        return context

class GeneralEdit(UpdateView):
    template_name = "general_form.html"
    def setting(self, model, title):
        self.title = title
        self.model = model

class GeneralAdd(CreateView):
    template_name = "general_form.html"
    def setting(self, model, title):
        self.title = title
        self.model = model

#class GeneralView:
    #def __init__(self, model, title):
        #self.List = ListView()
        #self.Edit = UpdateView()
        #self.Add = CreateView()
        #self.Delete = DeleteView()
        #self.Detail = DetailView()
        #self.model = model
        #self.template_name = template_name

class PersonList(GeneralList):
    def __init__(self):
        # スーパークラスの設定
        super(PersonList, self).setting(Person, "Person")

class PersonDetail(GeneralDetail):
    def __init__(self):
        # スーパークラスの設定
        super(PersonDetail, self).setting(Person, PersonForm, "Person")


class PersonEdit(GeneralEdit):
    def __init__(self):
        # スーパークラスの設定
        super(PersonEdit, self).setting(Person, "Person")

class PersonAdd(GeneralAdd):
    def __init__(self):
        # スーパークラスの設定
        super(PersonAdd, self).setting(Person, "Person")

class PersonListView(TemplateView):
    template_name = "person_list.html"

    def get(self, request, *args, **kwargs):
        context = super(PersonListView, self).get_context_data(**kwargs)

        persons = Person.objects.all()
        context ['persons'] = persons

        return render(self.request, self.template_name, context)


def person_delete(request, person_id):
    """Personの削除"""
    #return HttpResponse("Person削除")
    person = get_object_or_404(Person, pk=person_id)
    person.delete()
    return redirect('person_list2')

class ManagerListView(ListView):
    model = Manager
    template = "manager_list.html"