import tempfile
from django.conf import settings
from django.views.generic import FormView, ListView
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from file_upload.utils import get_download_link, upload_to_yandex_disk
from .forms import FileUploadForm
from .models import UploadedFile
import requests
import os


class FileUploadView(LoginRequiredMixin, FormView):
    template_name = "file_upload/upload_file.html"
    success_url = reverse_lazy("uploaded_files_list")
    form_class = FileUploadForm

    def form_valid(self, form):
        uploaded_file = self.request.FILES["file"]  # Получаем файл из формы
        folder_name = form.cleaned_data.get(
            "folder_name", ""
        ).strip()  # Получаем имя папки из формы

        # Если имя папки указано, создаём путь на Яндекс.Диске
        if folder_name:
            user_folder = f"/{folder_name}"
        else:
            user_folder = f"/"  # Папка по умолчанию BASE_DIR

        # Создаём временный файл
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            for chunk in uploaded_file.chunks():
                tmp_file.write(chunk)
            tmp_file_path = tmp_file.name

        # Загружаем файл на Яндекс.Диск
        success = upload_to_yandex_disk(tmp_file_path, uploaded_file.name, user_folder)

        # Удаляем временный файл
        os.remove(tmp_file_path)

        if success:
            yandex_path = f"{user_folder}/{uploaded_file.name}"
            download_link = get_download_link(yandex_path)
            # Сохраняем запись в базе данных
            UploadedFile.objects.create(
                user=self.request.user,
                file_name=uploaded_file.name,
                yandex_path=yandex_path,
                download_link=download_link,
            )
            return super().form_valid(form)
        else:
            return JsonResponse({"message": "Ошибка при загрузке файла"}, status=400)


class UploadedFilesListView(LoginRequiredMixin, ListView):
    """
    Представление для отображения списка загруженных файлов.
    Использует CBV ListView.
    """
    model = UploadedFile
    template_name = "file_upload/uploaded_files_list.html"
    context_object_name = "files"

    def get_queryset(self):
        """
        Возвращает только те файлы, которые существуют на Яндекс.Диске.
        """
        files = UploadedFile.objects.filter(user=self.request.user)
        valid_files = []

        headers = {"Authorization": f"OAuth {settings.YANDEX_DISK_TOKEN}"}
        yandex_api_url = "https://cloud-api.yandex.net/v1/disk/resources"

        for file in files:
            # Путь к файлу на Яндекс.Диске
            yandex_path = file.yandex_path

            # Проверяем существование файла через API
            response = requests.get(yandex_api_url, headers=headers, params={"path": yandex_path})
            if response.status_code == 200:
                # Файл существует, добавляем в список
                valid_files.append(file)
            elif response.status_code == 404:
                # Файл не существует, удаляем его из базы данных
                file.delete()

        return valid_files
