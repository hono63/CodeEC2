from django.forms import ModelForm
from manager.models import Person, Worker, Manager


class PersonForm(ModelForm):
    """Personのメタ(?)フォーム"""
    class Meta:
        model = Person
        fields = ('name', 'sex', )

class ManagerForm(ModelForm):
    """Managerフォーム"""
    class Meta:
        model = Manager
        fields = ('person', 'department', )

class WorkerForm(ModelForm):
    """Workerのフォーム"""
    class Meta:
        model = Worker
        fields = ('manager', 'person', )