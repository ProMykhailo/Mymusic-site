from django.db import models

class Track(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва треку")
    author = models.CharField(max_length=100, verbose_name="Виконавець")
    # Файли завантажуватимуться в папку media/tracks/
    audio_file = models.FileField(upload_to='tracks/', verbose_name="Аудіофайл")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Додано")

    def __str__(self):
        # Так трек красиво відображатиметься в майбутній адмінці
        return f"{self.author} - {self.title}"