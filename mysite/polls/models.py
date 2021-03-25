from django.db import models

# Create your models here.


class Ranking(models.Model):
    id = models.AutoField(primary_key=True)
    yearRange = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    type = models.CharField(max_length=500)
    total_number = models.FloatField()

    class Meta:
        verbose_name = "Ranking"
        db_table = "Ranking"
