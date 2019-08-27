from django.db import models

# Create your models here.

class Serie(models.Model):
    nom = models.CharField(max_length= 100)
    
    def __str__(self):
        return self.nom
    
    def get_products(self):
     return Produit.objects.filter(serie__nom=self.nom)

class Produit(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, null=True)
    image = models.FileField(upload_to="images/", default=False)

    def __str__(self):
        return self.title

    




    