from django.db import models
class Ishchi(models.Model):
    rasmi = models.ImageField()
    ismi = models.CharField(max_length = 300)
    familiyasi = models.CharField(max_length = 300)
    nima_qigan = models.TextField()
    qayerda_oqigan = models.CharField(max_length = 300, blank = True)
    ish_darajasi = models.CharField(max_length = 300)

    def __str__(self) -> str:
        return f'{self.ismi} {self.familiyasi}'

class Loyiha(models.Model):
    nomi = models.CharField(max_length = 400)  
    rasmi = models.ImageField()
    ishchi = models.ForeignKey('Ishchi', related_name="loyihalar", on_delete = models.CASCADE)
    kategoriya = models.ForeignKey('Kategoriya', on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.nomi

class Kategoriya(models.Model):
    nomi = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.nomi

     
# Create your models here.