from django.forms import fields
# here setting the attributes for the Model
from rest_framework import serializers

from leads.models import Post, Lead


# this is will convert model to json (Endpoint)
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title', 'description', 'agent_user'
        )


class LeadSerilezer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = (
            'first_name', 'last_name', 'agent'
        )
