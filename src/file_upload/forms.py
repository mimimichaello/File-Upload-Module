from django import forms

class FileUploadForm(forms.Form):
    file = forms.FileField(label="Выберите файл")  # Поле для загрузки файла
    folder_name = forms.CharField(
        label="Имя папки",
        max_length=255,
        required=False,
        help_text="Введите имя папки на Яндекс.Диске (необязательно)"
    )
