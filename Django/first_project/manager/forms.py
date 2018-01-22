from django.forms import ModelForm
from manager.models import Person


class PersonForm(ModelForm):
    """Personのメタ(?)フォーム"""
    class Meta:
        model = Person
        fields = ('name', 'sex', )