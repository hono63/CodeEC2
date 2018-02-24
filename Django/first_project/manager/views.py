from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DetailView, DeleteView
from django.forms.models import model_to_dict
from django.core import serializers
from django.urls import reverse_lazy

from manager.models import Person, Worker, Manager
from manager.forms import PersonForm, ManagerForm, WorkerForm

# Create your views here.
#get_object_404(Person, id=20)

def get_global_name(ram):
    "global変数の名前を取得する"
    name = str("")
    for k,v in globals().items():
        if id(ram) == id(v):
            name = k
            break
    return name

class GeneralList(ListView):
    template_name = "general_list.html"

    def setting(self, model):
        self.model = model
        self.name = get_global_name(model).lower()
        self.labels = self.model._meta.get_fields(include_parents=True, include_hidden=True)

    def get_context_data(self, **kwargs):
        """
        Detailと同じような方法ではできない。
        参考：
        https://stackoverflow.com/questions/2170228/iterate-over-model-instance-field-names-and-values-in-template
        https://docs.djangoproject.com/en/2.0/topics/serialization/
        """
        context = super().get_context_data(**kwargs)
        # オブジェクト
        serial = serializers.serialize( "python", self.model.objects.all() )
        context ['serial'] = serial
        context ['label'] = self.labels
        # 名前など
        context ['title'] = self.name.capitalize()
        context ['add_page'] = self.name + "-add-page"
        context ['edit_page'] = self.name + "-edit-page"
        context ['detail_page'] = self.name + "-detail-page"

        return context

class GeneralDetail(DetailView):
    template_name = "general_detail.html"

    def setting(self, model):
        self.model = model
        self.name = get_global_name(model).lower()

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
        # 名前など
        context ['title'] = self.name.capitalize()
        context ['edit_page'] = self.name + "-edit-page"
        context ['list_page'] = self.name + "-list-page"
        context ['delete_page'] = self.name + "-delete-page"

        return context

class GeneralEdit(UpdateView):
    template_name = "general_form.html"

    def setting(self, model, form):
        self.model = model
        self.form_class = form
        self.name = get_global_name(model).lower()
        self.success_url = reverse_lazy(self.name + "-list-page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 名前など
        context ['title'] = self.name.capitalize()
        context ['list_page'] = self.name + "-list-page"
        context ['delete_page'] = self.name + "-delete-page"
        return context

class GeneralAdd(CreateView):
    template_name = "general_form.html"

    def setting(self, model, form):
        self.model = model
        self.form_class = form
        self.name = get_global_name(model).lower()
        self.success_url = reverse_lazy(self.name + "-list-page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 名前など
        context ['title'] = self.name.capitalize()
        context ['list_page'] = self.name + "-list-page"
        return context

class GeneralDelete(DeleteView):
    template_name = "general_delete.html"

    def setting(self, model):
        self.model = model
        self.name = get_global_name(model).lower()
        self.success_url = reverse_lazy(self.name + "-list-page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 名前など
        context ['title'] = self.name.capitalize()
        context ['detail_page'] = self.name + "-detail-page"
        return context

# PersonのView
class PersonList(GeneralList):
    def __init__(self):
        # スーパークラスの設定
        super().setting(Person)

class PersonDetail(GeneralDetail):
    def __init__(self):
        super().setting(Person)

class PersonEdit(GeneralEdit):
    def __init__(self):
        super().setting(Person, PersonForm)

class PersonAdd(GeneralAdd):
    def __init__(self):
        super().setting(Person, Person)

class PersonDelete(GeneralDelete):
    def __init__(self):
        super().setting(Person)

# ManagerのView
class ManagerList(GeneralList):
    def __init__(self):
        super().setting(Manager)

class ManagerDetail(GeneralDetail):
    def __init__(self):
        super().setting(Manager)

class ManagerEdit(GeneralEdit):
    def __init__(self):
        super().setting(Manager, ManagerForm)

class ManagerAdd(GeneralAdd):
    def __init__(self):
        super().setting(Manager, ManagerForm)

class ManagerDelete(GeneralDelete):
    def __init__(self):
        super().setting(Manage)

# WorkerのView
class WorkerList(GeneralList):
    def __init__(self):
        super().setting(Worker)

class WorkerDetail(GeneralDetail):
    def __init__(self):
        super().setting(Worker)

class WorkerEdit(GeneralEdit):
    def __init__(self):
        super().setting(Worker, WorkerForm)

class WorkerAdd(GeneralAdd):
    def __init__(self):
        super().setting(Worker, WorkerForm)

class WorkerDelete(GeneralDelete):
    def __init__(self):
        super().setting(Worker)