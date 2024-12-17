# Django File Upload Module with Yandex.Disk Integration

Этот проект реализует модуль загрузки файлов на **Яндекс.Диск** с использованием **Django**. Пользователи могут загружать файлы, создавать папки, а также получать ссылки для скачивания.

---

## **Функционал**

1. **Загрузка файлов** на Яндекс.Диск.
2. **Создание папок** на Яндекс.Диске для организации файлов.
3. **Отображение списка файлов**, загруженных пользователем.
4. **Получение ссылок для скачивания файлов** напрямую с Яндекс.Диска.
5. Красивый интерфейс с использованием **DaisyUI** и **TailwindCSS**.
6. Анимация загрузки с **спиннером** при отправке файла.

---

## **Стек технологий**

- **Backend**: Django 4.x
- **Frontend**: TailwindCSS + DaisyUI
- **Cloud Storage**: Yandex.Disk API
- **Database**: SQLite (по умолчанию)
- **Python**: 3.11+

---

## **Установка проекта**

### **1. Клонирование репозитория**

```bash
git clone https://github.com/mimimichaello/File-Upload-Module.git
cd django-yandex-upload
```

### **2. Создание виртуального окружения**

```bash
python -m venv venv
source venv/bin/activate    # Для Linux/Mac
venv\Scripts\activate       # Для Windows
```

### **3. Установка зависимостей**

```bash
pip install -r requirements.txt
```

### **3. Настройка переменных окружения**
Создайте файл .env в корневой директории проекта.
Добавьте следующие переменные окружения:

```python
YANDEX_DISK_TOKEN=ваш_токен_от_яндекс.диска
SECRET_KEY=ваш_django_secret_key
DEBUG=True
```

## **Запуск проекта**

### **1. Применение миграций**

```bash
python manage.py makemigrations
python manage.py migrate
```

### **2. Создание суперпользователя**

```bash
python manage.py createsuperuser
```
### **3. Запуск сервера разработки**

```bash
python manage.py runserver
```

## **Использование**

### **Загрузка файлов**
Перейдите на страницу "Загрузить файл" по адресу:  `http://127.0.0.1:8000/upload/`

Выберите файл для загрузки и укажите имя папки (необязательно).
Нажмите кнопку "Загрузить". Появится спиннер, показывающий процесс загрузки.

### **Просмотр загруженных файлов**
Перейдите на страницу "Ваши загруженные файлы" по адресу:  `http://127.0.0.1:8000/files/`

Отобразится таблица с файлами, содержащая:
- Имя файла.
- Путь на Яндекс.Диске.
- Дату загрузки.
- Кнопку "Скачать" для получения ссылки на скачивание файла.

## **Структура проекта**
```textcode();
file_upload_module/
│
├── file_upload/                  # Приложение загрузки файлов
│   ├── migrations/               # Миграции БД
│   ├── templates/                # HTML-шаблоны
│   │   ├── file_upload/
│   │       ├── upload_file.html  # Шаблон для загрузки файла
│   │       ├── uploaded_files_list.html  # Шаблон списка файлов
│   ├── forms.py                  # Форма для загрузки файла
│   ├── models.py                 # Модель UploadedFile
│   ├── views.py                  # Представления
│   └── urls.py                   # URL-маршруты
│
├── core/                         # Основное приложение с базовым шаблоном
│   ├── templates/core/
│   │   ├── base.html             # Базовый шаблон с Navbar
│
├── manage.py                     # Файл для управления Django-проектом
└── requirements.txt              # Зависимости проекта
```