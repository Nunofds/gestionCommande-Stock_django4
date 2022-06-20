from django.forms import ModelForm
from .models import Command


class CommandForm(ModelForm):
    class Meta:
        model = Command
        fields = '__all__'
