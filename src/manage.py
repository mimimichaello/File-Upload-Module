import os
import sys
from pathlib import Path

def main():
    """Run administrative tasks."""
    # Устанавливаем путь к настройкам Django в src/core/settings.py
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

    # Добавляем src в PYTHONPATH, чтобы Python нашёл модуль core
    BASE_DIR = Path(__file__).resolve().parent
    sys.path.append(str(BASE_DIR))

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
