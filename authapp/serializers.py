from .models import Students
from rest_framework import serializers

class StudentSeri(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields="__all__"