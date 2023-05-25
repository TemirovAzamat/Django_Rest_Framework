from rest_framework import serializers

from .models import Doctor, Patient


class DoctorSerializer(serializers.Serializer):
    name = serializers.CharField()
    work_experience = serializers.IntegerField()

    def create(self, validated_data):
        return Doctor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.work_experience = validated_data['work_experience']
        return instance


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
