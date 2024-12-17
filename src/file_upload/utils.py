from django.conf import settings
import requests


def create_folder_on_yandex_disk(folder_path):
    """
    Создаёт папку на Яндекс.Диске по указанному пути.
    """
    headers = {"Authorization": f"OAuth {settings.YANDEX_DISK_TOKEN}"}
    url = "https://cloud-api.yandex.net/v1/disk/resources"

    # Отправляем PUT-запрос для создания папки
    response = requests.put(url, headers=headers, params={"path": folder_path})

    if response.status_code == 201:
        print(f"Папка {folder_path} успешно создана")
        return True
    elif response.status_code == 409:
        print(f"Папка {folder_path} уже существует")
        return True
    else:
        print(f"Ошибка при создании папки {folder_path}: {response.status_code}")
        return False


def upload_to_yandex_disk(file_path, file_name, folder_path):
    """Загружает файл на Яндекс.Диск."""
    create_folder_on_yandex_disk(folder_path)

    # Формируем путь для файла внутри папки
    full_path = f"{folder_path}/{file_name}"

    headers = {"Authorization": f"OAuth {settings.YANDEX_DISK_TOKEN}"}
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"

    # Получаем URL для загрузки файла
    params = {"path": full_path, "overwrite": "true"}
    response = requests.get(upload_url, headers=headers, params=params)

    if response.status_code == 200:
        href = response.json()["href"]
        with open(file_path, "rb") as f:
            upload_response = requests.put(href, files={"file": f})
            return upload_response.status_code == 201
    return False


def get_download_link(yandex_path):
    """
    Получает временную ссылку для скачивания файла с Яндекс.Диска.
    """
    headers = {"Authorization": f"OAuth {settings.YANDEX_DISK_TOKEN}"}
    download_url = "https://cloud-api.yandex.net/v1/disk/resources/download"

    # Запрашиваем ссылку для скачивания
    params = {"path": yandex_path}
    response = requests.get(download_url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json().get("href")  # Возвращаем временную ссылку
    return None
