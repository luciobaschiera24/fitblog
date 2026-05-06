from django.db import models
from ckeditor.fields import RichTextField

class Routine(models.Model):
    CATEGORY_CHOICES = [
        ('pecho', 'Pecho'),
        ('espalda', 'Espalda'),
        ('piernas', 'Piernas'),
        ('brazos', 'Brazos'),
        ('hombros', 'Hombros'),
        ('cardio', 'Cardio'),
        ('fullbody', 'Full Body'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    description = RichTextField()
    image = models.ImageField(upload_to='routines/')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Rutina'
        verbose_name_plural = 'Rutinas'

    def __str__(self):
        return self.title
    