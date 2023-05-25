from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .serializers import PatientSerializer, DoctorSerializer
from .models import Patient, Doctor
from .my_generic import MyGenericRetrieveUpdateDestroyAPIView


@api_view(http_method_names=['GET', 'POST'])
def doctor_list_create_api_view(request):
    """
    Doctor List and Create View
    :param limit: int
    """
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(instance=doctors, many=True)
        return Response(serializer.data, status=200)

    if request.method == 'POST':
        received_data = request.data
        serializer = DoctorSerializer(data=received_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)


class DoctorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Doctor Retrieve, Update and Destroy View
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


@api_view(http_method_names=['GET', 'POST'])
def patient_list_create_api_view(request):
    """
    Patient List and Create View
    :param limit: int
    """
    if request.method == 'GET':
        patient = Patient.objects.all()
        serializer = PatientSerializer(instance=patient, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class PatientRetrieveUpdateDestroyAPIView(MyGenericRetrieveUpdateDestroyAPIView):
    """
    Patient Retrieve, Update and Destroy View
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
