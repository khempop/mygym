from rest_framework import serializers
from gym.models import Gym

# class GymSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     status = serializers.BooleanField(default=False)

#     def create(self, validated_data):
#         """
#         Create and return a new `gym` instance, given the validated data.
#         """
#         return Gym.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Gym` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.code = validated_data.get('code', instance.code)
#         instance.status = validated_data.get('status', instance.status)
#         instance.save()
#         return instance

#     def view(self, instance):
#         """
#         Query and return an existing `Gym` instance.
#         """
#         id = instance.id
#         return User.objects.filter(id=id)

# username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
# email = models.EmailField(('email address'), unique = True)
# created = models.DateTimeField(auto_now_add=True)
# firstname = models.CharField(max_length=100, blank=True, default='')
# lastname = models.CharField(max_length=100, blank=True, default='')
# code = models.TextField(blank=True, default='')
# stripeid = models.CharField(max_length=200, blank=True)
# status = models.BooleanField(default=False)
class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = "__all__"