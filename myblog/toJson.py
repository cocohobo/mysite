from rest_framework import fields, serializers
from myblog.models import Classes,UserInfo

class Classes_data(serializers.ModelSerializer):
    class Meta:
        depth=1
        model=Classes
        fields = '__all__'

class Userinfo_data(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = UserInfo
        fields = '__all__'