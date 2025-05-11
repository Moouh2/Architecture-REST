from rest_framework import serializers
from .models import Patient, Medecin, RendezVous, Consultation

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class MedecinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medecin
        fields = '__all__'

class RendezVousSerializer(serializers.ModelSerializer):
    patient_nom = serializers.StringRelatedField(source='patient', read_only=True)
    medecin_nom = serializers.StringRelatedField(source='medecin', read_only=True)

    class Meta:
        model = RendezVous
        fields = ['id', 'patient', 'medecin', 'date', 'statut', 'patient_nom', 'medecin_nom']

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'
