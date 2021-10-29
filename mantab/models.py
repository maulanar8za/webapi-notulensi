from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class asisten(models.Model):
    jdl= models.CharField('Judul Rapat', max_length=50)
    notul = models.CharField('Notulen',max_length=50)
    isi = models.CharField('Notulensi', max_length=400)
    tanggal = models.DateField()
    ass = models.CharField('Asisten Hadir', max_length=1000)
    def __str__(self):
        return self.jdl