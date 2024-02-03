from rest_framework import serializers
from baseApp.models import Tools


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tools
        fields = "__all__"