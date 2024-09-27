from rest_framework import serializers
from .models import Employers


class EmployerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employers
        fields = ['id','first_name','last_name','email','phone_no']


