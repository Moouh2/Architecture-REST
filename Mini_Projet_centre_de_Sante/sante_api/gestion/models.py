from django.db import models

# Create your models here.

class Patient(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    adresse = models.TextField()
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Medecin(models.Model):
    nom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)

    def __str__(self):
        return f"Dr. {self.nom} ({self.specialite})"

class RendezVous(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    date = models.DateTimeField()
    statut = models.CharField(max_length=20, default="En attente")

    def __str__(self):
        return f"{self.patient} avec {self.medecin} le {self.date.strftime('%d/%m/%Y %H:%M')}"

class Consultation(models.Model):
    rendez_vous = models.OneToOneField(RendezVous, on_delete=models.CASCADE)
    diagnostic = models.TextField()
    traitement = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Consultation du {self.date} - {self.rendez_vous}"
