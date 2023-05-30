from django.db import models

class Kategoriak(models.Model):
    nev = models.CharField( max_length=50, verbose_name = 'nev')


    def __str__(self):
        return self.nev

class Recept(models.Model):
    nev = models.CharField( max_length=50, verbose_name = 'nev')
    kat_id = models.ForeignKey(Kategoriak, verbose_name= "kategoria_id", on_delete=models.CASCADE)
    kep_eleresi_ut	= models.CharField(max_length=50, verbose_name = 'kep eleresi ut')
    leiras = models.TextField(verbose_name="leiras")
    hirdetes_datuma = models.DateField(null = True, blank = True, verbose_name = 'hirdetes datuma')

    def __str__(self):
        return self.nev