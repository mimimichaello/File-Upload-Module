from django.db import models
from django.contrib.auth.models import User

class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="uploaded_files")
    file_name = models.CharField(max_length=255)  # Имя файла
    yandex_path = models.CharField(max_length=500)  # Путь на Яндекс.Диске
    download_link = models.URLField(max_length=1000, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Дата загрузки

    def __str__(self):
        return f"{self.file_name} (Пользователь: {self.user.username})"
