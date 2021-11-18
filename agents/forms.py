from django.forms import fields, forms, ModelForm, models
from leads.models import Agent


class AgentModelForm(ModelForm):
    class Meta:
        model = Agent
        fields = (
            'user',
        )
